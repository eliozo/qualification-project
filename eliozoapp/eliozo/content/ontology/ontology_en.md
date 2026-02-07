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
