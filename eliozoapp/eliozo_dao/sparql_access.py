class SparqlAccess:
    fuseki_url = 'NA'

    def __init__(self, fuseki_url): 
        self.fuseki_url = fuseki_url

    def get_message(self): 
        return f'Hello {self.fuseki_url}'

