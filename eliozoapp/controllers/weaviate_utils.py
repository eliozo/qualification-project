import os
from dotenv import load_dotenv
from rdflib import Graph, URIRef, Namespace, RDF
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
import sys
import requests
import asyncio
#from weaviate import WeaviateAsyncClient
from weaviate import WeaviateAsyncClient


class WeaviateUtils:
    weaviate_url = "NA"
    weaviate_api_key = "NA"
    openai_api_key = "NA"
    # RDF namespace to find relevant items in Turtle files
    eliozoNS = Namespace("http://www.dudajevagatve.lv/eliozo#")
    # Weaviate client initialized in constructor __init__(...), see below
    client = None
    skipping_mode = False

    def __init__(self, weaviate_url, weaviate_api_key, openai_api_key): 
        self.weaviate_url = weaviate_url
        self.weaviate_api_key = weaviate_api_key
        self.openai_api_key = openai_api_key

        self.client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=Auth.api_key(weaviate_api_key),
            headers={
                "X-OpenAI-Api-Key": openai_api_key
            },
            skip_init_checks=True
        )

    def close_client(self):
        if self.client is not None: 
            self.client.close()
            self.client = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_client()

    def set_skipping_mode(self, skipping_mode):
        self.skipping_mode = skipping_mode
 
    def drop_collections(self):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)

        for collection_name in ["Problem", "Olympiad", "Classifier"]:
            try:
                # Use v4 client to delete
                self.client.collections.delete(collection_name)
                print(f"Dropped collection: {collection_name}")
            except Exception as e:
                # We expect it might fail if it doesn't exist, though the client handles it gracefully usually?
                # Actually v4 delete usually returns None. If it fails (e.g. connection), it raises.
                print(f"Error dropping {collection_name}: {e}")

        return (0, {'keyNN':'drop_collections'})

    
    def _get_schema_config(self):
        """Returns the configuration for all collections."""
        return {
            "Classifier": {
                "name": "Classifier",
                "properties": [
                    wc.Property(name="property", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="label", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="shortName", data_type=wc.DataType.TEXT), 
                    wc.Property(name="description", data_type=wc.DataType.TEXT)
                ],
                "vectorizer_config": wc.Configure.Vectorizer.text2vec_openai(),
                "generative_config": wc.Configure.Generative.openai()
            },
            "Olympiad": {
                "name": "Olympiad",
                "properties": [
                    wc.Property(name="olympiadCode", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="olympiadCountry", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="olympiadDescription_en", data_type=wc.DataType.TEXT), 
                    wc.Property(name="olympiadDescription_lt", data_type=wc.DataType.TEXT), 
                    wc.Property(name="olympiadDescription_lv", data_type=wc.DataType.TEXT), 
                    wc.Property(name="olympiadID", data_type=wc.DataType.TEXT, skip_vectorization=True),
                    wc.Property(name="olympiadName_en", data_type=wc.DataType.TEXT),
                    wc.Property(name="olympiadName_lt", data_type=wc.DataType.TEXT),
                    wc.Property(name="olympiadName_lv", data_type=wc.DataType.TEXT)
                ],
                "vectorizer_config": wc.Configure.Vectorizer.text2vec_openai(),
                "generative_config": wc.Configure.Generative.openai()
            },
            "Problem": {
                "name": "Problem",
                "properties": [
                    wc.Property(name="problemID", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="problemGrade", data_type=wc.DataType.INT, skip_vectorization=True), 
                    wc.Property(name="problemText_lv", data_type=wc.DataType.TEXT), 
                    wc.Property(name="solutionText_lv", data_type=wc.DataType.TEXT), 
                    wc.Property(name="olympiadType", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                    wc.Property(name="problemYear", data_type=wc.DataType.INT, skip_vectorization=True)
                ],
                "vectorizer_config": wc.Configure.Vectorizer.text2vec_openai(),
                "generative_config": wc.Configure.Generative.openai()
            }
        }

    # This function attempts to create collections "Olympiad", "Problem", "Classifier"
    # If they already exist, then there are no changes (and a message is printed). 
    def create_schema(self):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)
        
        # Remove broad try/except to reveal errors
        existing_collections = self.client.collections.list_all()
        print(f"Existing collections before creation: {list(existing_collections.keys())}")
        
        schema_config = self._get_schema_config()

        for collection_name, config in schema_config.items():
            if collection_name in existing_collections:
                print(f"Collection '{collection_name}' already exists; skip creation")
            else:
                print(f"Creating collection '{collection_name}'")
                new_collection = self.client.collections.create(
                    name=config["name"], 
                    properties=config["properties"],
                    vectorizer_config=config["vectorizer_config"],
                    generative_config=config["generative_config"]
                )
                print(f"Created: {new_collection.name}")

        return (0, {'keyNN':'create_schema'})



    def ingest_to_weaviate(self, filename):
        print(f'Importing {filename} to  Weaviate')
        graph = Graph()
        graph.parse(filename, format="ttl")

        if not self.client.is_ready():
            print('Weaviate client is not ready!')
            sys.exit(1)


        problemCount = 0
        for subj in graph.subjects(predicate=RDF.type, 
                                    object=self.eliozoNS.Problem):

            problemID = "NA"
            olympiadType = "NA"
            problemGrade = 0
            problemYear = 0

            try:
                val = graph.value(subj, self.eliozoNS.problemID)
                problemID = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {problemCount}; skipping insert")
                continue
            problemCount += 1
            print(f'Ingesting {problemID}...')
            # Extract properties that don't require language specification


            try:
                val = graph.value(subj, self.eliozoNS.olympiadType)
                olympiadType = str(val)
            except Exception as e:
                print(f"Error converting olympiadType={val} for {problemCount}; skipping insert")
                continue


            try: 
                val = graph.value(subj, self.eliozoNS.problemGrade)
                problemGrade = int(val)
            except Exception as e:
                print(f"Error converting problemGrade={val} for {problemCount}; skipping insert")
                continue

            try: 
                val = graph.value(subj, self.eliozoNS.problemYear)
                problemYear = int(val)
            except Exception as e:
                print(f"Error converting problemYear={val} for {problemCount}; skipping insert")
                continue



            # Initialize the data object with non-language properties
            data_object = {
                "problemID": problemID,
                "problemGrade": problemGrade, 
                "olympiadType": olympiadType, 
                "problemYear": problemYear
            }
            # print(f'data_object = {data_object}')


            for lang in ['lv']:
                for obj in graph.objects(subj, self.eliozoNS.problemText):
                    if obj.language == lang:
                        data_object[f"problemText_{lang}"] = str(obj)

                for solution_obj in graph.objects(subj, self.eliozoNS.problemSolution): 
                    for solution_text in graph.objects(solution_obj, self.eliozoNS.solutionText):
                        if solution_text.language == lang:
                            if f"solutionText_{lang}" in data_object:
                                data_object[f"solutionText_{lang}"] = data_object[f"solutionText_{lang}"] + '\n\n' + str(solution_text)
                            else:
                                data_object[f"solutionText_{lang}"] = str(solution_text)
                
            if not self.skipping_mode:
                olympiads_collection = self.client.collections.get("Problem")

                olympiads_collection.data.insert(
                    properties=data_object,
                    references={}
                )
        return (0, {'keyMM':'ingest_to_weaviate'})
    

    # Currently only imports property=topic
    def ingest_classifier_data(self, property, filename):
        print(f'Importing classifier {property} to Weaviate')
        graph = Graph()
        graph.parse(filename, format="ttl")

        if not self.client.is_ready():
            print('Weaviate client is not ready!')
            sys.exit(1)

        print(f"Found triples: {len(graph)}")
        itemCount = 0

        for subj in graph.subjects(predicate=RDF.type, 
                                    object=self.eliozoNS.Topic):
            
            topicNumber = "X.X.X.X.X"
            try:
                val = graph.value(subj, self.eliozoNS.topicNumber)
                topicNumber = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {itemCount}; skipping insert")
                continue
            if topicNumber.endswith(".0.0.0.0"):
                print(f"skipping {topicNumber}")
                continue
            
            if (topicNumber.startswith("2.") or topicNumber.startswith("4.")) and topicNumber.endswith(".0.0.0"): 
                print(f"skipping {topicNumber}")
                continue

            if (topicNumber.startswith("1.") or topicNumber.startswith("3.")) and not topicNumber.endswith(".0.0.0"): 
                print(f"skipping {topicNumber}")
                continue

            if not topicNumber.endswith("0.0"):
                print(f"skipping {topicNumber}")
                continue



            label = "NA"
            shortName = "NA"
            description = "NA"

            try:
                val = graph.value(subj, self.eliozoNS.topicID)
                label = str(val)
                val = graph.value(subj, self.eliozoNS.topicName)
                shortName = str(val)
                val = graph.value(subj, self.eliozoNS.topicDescription)
                description = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {itemCount}; skipping insert")
                continue
            itemCount += 1
            print(f'Ingesting {itemCount}...')
            # Extract properties that don't require language specification


            # Initialize the data object with non-language properties
            data_object = {
                "property": property,
                "label": label, 
                "shortName": shortName, 
                "description": description
            }
            #print(f'data_object = {data_object}')

            classifiers_collection = self.client.collections.get("Classifier")

            classifiers_collection.data.insert(
                properties=data_object,
                references={}
            )
        # self.client.close()  <-- removed
        return (0, {'keyMM':'ingest_to_weaviate'})
    


    # Private method called by "find_problems"
    def near_search(self, collection, myquery, mylimit): 
        # Check if collection exists
        if not self.client.collections.exists(collection):
            raise Exception(f"Collection '{collection}' does not exist.")
            
        problems = self.client.collections.get(collection)
        print(f'Searching query "{myquery}" with limit "{mylimit}"')
        response = problems.query.near_text(
            query=myquery,
            limit=mylimit,
            return_metadata=MetadataQuery(distance=True), 
        )
        result = []
        for o in response.objects:
            result.append(o.properties)
        return result
        

    def get_problems(self, query, mylimit):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)
        results = []
        try:
            # Replaced "Problems" typoe with "Problem"
            results = self.near_search("Problem", query, mylimit)
        except Exception as e:
            # We want to propagate the "not exist" error, or handle it? 
            # The prompt says: "get_problems(...) should return an exception telling that the collections do not exist."
            # So we re-raise or just let it bubble up.
            print(f"Error in get_problems: {e}")
            raise e
        return (0, {'problems':results})



