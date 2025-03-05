Each data model comes with its own query language or framework, and we discussed several examples:
SQL, MapReduce, MongoDB’s aggregation pipeline, Cypher, SPARQL, and Datalog. We also touched on CSS
and XSL/XPath, which aren’t database query languages but have interesting parallels. Although we have covered a lot of ground, there are still many data models left unmentioned. To give
just a few brief examples: *  
Researchers working with genome data often need to perform sequence-similarity searches, which
means taking one very long string (representing a DNA molecule) and matching it against a large
database of strings that are similar, but not identical. None of the databases described here can
handle this kind of usage, which is why researchers have written specialized genome database
software like GenBank [[48](ch02.html#Benson2007de)]. *  
Particle physicists have been doing Big Data–style large-scale data analysis for decades, and
projects like the Large Hadron Collider (LHC) now work with hundreds of petabytes! At such a scale
custom solutions are required to stop the hardware cost from spiraling out of control
[[49](ch02.html#Rademakers2013vu)].