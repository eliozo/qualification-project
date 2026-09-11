We use the 2020 Mathematics Subject Classification (MSC2020) for categorizing mathematical problems and concepts.  
[View the 2020 Mathematics Subject Classification](https://mathscinet.ams.org/mathscinet/msc/msc2020.html)

**RDF Structure:**  
This ontology treats **Solution** as a first-class entity (a node) rather than just a property value of the entity **Problem**.

* **Problem Node**
    * `hasDomainTopic` &rarr; "Integer Equations"
    * `hasStatement` &rarr; "Find all $x, y \in \mathbb{Z}$..."
    * `hasSolution` &rarr; Solution_Alpha (Node)
    * `hasSolution` &rarr; Solution_Beta (Node)
* **Solution Node (e.g., Solution_Alpha)**
    * `requiresResult` &rarr; "Fermat's Little Theorem"
    * `employsStrategy` &rarr; "Proof by Contradiction"
    * `difficultyLevel` &rarr; "High"


**Jēdzienu vārdnīca:** 

* Latvijas pamatskolas standarts (Latvian primary school standard)
* Latvijas vidusskolas standards (Latvian high-school standard)
* Programmu paraugi. 
* Nodarbību sadaļa (curriculum unit, turinio skyrius), sk. `programma_old.csv`, 
  `programma_new.csv`, `standarts.csv` (prefikss `LO_`)
* Mācīšanās rezultāts (Learning outcome, mokymosi rezultatas), 
  sk. `programma_old.csv`, `programma_new.csv`, `standarts.csv`prefikss `LO_`); 
  sal. [EQF](https://europass.europa.eu/en/european-qualifications-framework-eqf).
* Satura temats (turinio tema, content topic), sk. `topics.csv`, prefikss `TO_`. 
  Topics atbild uz jautājumu par ko ir uzdevums (priekšmetiskais saturs). 
* Modelis (model). 
  kādu matemātisko konstrukciju risinātājs uzbūvē atrisinājumā.


**Par tematiem:** 

Tēzauru standartā ISO 25964 ir `NodeRole` (`Assignable`, vai `Category` - tikai bērnu grupēšanai, bet nevar to piešķirt 
uzdevumam). 
