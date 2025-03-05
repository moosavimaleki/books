2.  Another vertex in the graph. In that case, the predicate is an edge in the
graph, the subject is the tail vertex, and the object is the head vertex. For example, in
(lucy, marriedTo, alain) the subject and object lucy and alain are both vertices, and
the predicate marriedTo is the label of the edge that connects them. [Example 2-6](#fig_graph_n3_triples) shows the same data as in [Example 2-3](#fig_cypher_create), written as
triples in a format called Turtle, a subset of Notation3 (N3)
[[39](ch02.html#Beckett2011vq)]. ##### Example 2-6. A subset of the data in [Figure 2-5](#fig_datamodels_graph), represented as Turtle triples ```
@prefix : .
_:lucy     a       :Person.
_:lucy     :name   "Lucy".
_:lucy     :bornIn _:idaho.
_:idaho    a       :Location.
_:idaho    :name   "Idaho".
_:idaho    :type   "state".
_:idaho    :within _:usa.
_:usa      a       :Location.
_:usa      :name   "United States".
_:usa      :type   "country".
_:usa      :within _:namerica.
_:namerica a       :Location.
_:namerica :name   "North America".
_:namerica :type   "continent".
``` In this example, vertices of the graph are written as _:someName. The name doesn’t mean anything
outside of this file; it exists only because we otherwise wouldn’t know which triples refer to the
same vertex. When the predicate represents an edge, the object is a vertex, as in _:idaho :within
_:usa.  When the predicate is a property, the object is a string literal, as in _:usa :name
"United States".