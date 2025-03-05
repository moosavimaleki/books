```
`CREATE` `TABLE` `vertices` `(`
    `vertex_id`   `integer` `PRIMARY` `KEY``,`
    `properties`  `json`
`);`

`CREATE` `TABLE` `edges` `(`
    `edge_id`     `integer` `PRIMARY` `KEY``,`
    `tail_vertex` `integer` `REFERENCES` `vertices` `(``vertex_id``),`
    `head_vertex` `integer` `REFERENCES` `vertices` `(``vertex_id``),`
    `label`       `text``,`
    `properties`  `json`
`);`

`CREATE` `INDEX` `edges_tails` `ON` `edges` `(``tail_vertex``);`
`CREATE` `INDEX` `edges_heads` `ON` `edges` `(``head_vertex``);`
``` Some important aspects of this model are: 1.  Any vertex can have an edge connecting it with any other vertex. There is no schema that
restricts which kinds of things can or cannot be associated. 2.  Given any vertex, you can efficiently find both its incoming and its outgoing edges, and thus
traverse the graph—i.e., follow a path through a chain of vertices—both forward and backward.
(That’s why [Example 2-2](#fig_graph_sql_schema) has indexes on both the tail_vertex and head_vertex
columns.) 3.  By using different labels for different kinds of relationships, you can store several different
kinds of information in a single graph, while still maintaining a clean data model.