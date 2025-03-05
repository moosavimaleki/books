# Graph-Like Data Models 
We saw earlier that many-to-many relationships are an important distinguishing feature between
different data models. If your application has mostly one-to-many relationships (tree-structured
data) or no relationships between records, the document model is appropriate. 
But what if many-to-many relationships are very common in your data? The relational model can handle
simple cases of many-to-many relationships, but as the connections within your data become more
complex, it becomes more natural to start modeling your data as a graph. 
A graph consists of two kinds of objects: vertices (also known as nodes or entities) and
edges (also known as relationships or arcs). Many kinds of data can be modeled as a graph.
Typical examples include: Social graphs Vertices are people, and edges indicate which people know each other. The web graph Vertices are web pages, and edges indicate HTML links to other pages. Road or rail networks Vertices are junctions, and edges represent the roads or railway lines between them.