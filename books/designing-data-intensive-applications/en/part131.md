The structure is very similar. The following two expressions are equivalent (variables start with a
question mark in SPARQL): ```
(person) -[:BORN_IN]-> () -[:WITHIN*0..]-> (location)   # Cypher

?person :bornIn / :within* ?location.                   # SPARQL
``` Because RDF doesn’t distinguish between properties and edges but just uses predicates for both, you
can use the same syntax for matching properties. In the following expression, the variable usa is
bound to any vertex that has a name property whose value is the string "United States": ```
(usa {name:'United States'})   # Cypher

?usa :name "United States".    # SPARQL
``` SPARQL is a nice query language—even if the semantic web never happens, it can be a powerful tool
for applications to use internally. ##### Graph Databases Compared to the Network Model 
In [“Are Document Databases Repeating History?”](#sec_datamodels_codasyl) we discussed how CODASYL and the relational model competed to solve
the problem of many-to-many relationships in IMS. At first glance, CODASYL’s network model looks
similar to the graph model. Are graph databases the second coming of CODASYL in disguise?