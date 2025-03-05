*  A set of outgoing edges *  A set of incoming edges *  A collection of properties (key-value pairs) 
Each edge consists of: *  A unique identifier *  The vertex at which the edge starts (the tail vertex) *  The vertex at which the edge ends (the head vertex) *  A label to describe the kind of relationship between the two vertices *  A collection of properties (key-value pairs) 
You can think of a graph store as consisting of two relational tables, one for vertices and one for
edges, as shown in [Example 2-2](#fig_graph_sql_schema) (this schema uses the PostgreSQL json datatype to
store the properties of each vertex or edge). The head and tail vertex are stored for each edge; if
you want the set of incoming or outgoing edges for a vertex, you can query the edges table by
head_vertex or tail_vertex, respectively. ##### Example 2-2. Representing a property graph using a relational schema