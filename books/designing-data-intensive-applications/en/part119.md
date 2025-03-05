When all the vertices and edges of [Figure 2-5](#fig_datamodels_graph) are added to the database, we can start
asking interesting questions: for example, find the names of all the people who emigrated from the
United States to Europe. To be more precise, here we want to find all the vertices that have a BORN_IN edge to a
location within the US, and also a LIVING_IN edge to a location within Europe, and return the
name property of each of those vertices. [Example 2-4](#fig_cypher_query) shows how to express that query in Cypher. The same arrow notation is used in a
MATCH clause to find patterns in the graph: (person) -[:BORN_IN]-> () matches any two vertices
that are related by an edge labeled BORN_IN. The tail vertex of that edge is bound to the
variable person, and the head vertex is left unnamed. ##### Example 2-4. Cypher query to find people who emigrated from the US to Europe