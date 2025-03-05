
Well-known algorithms can operate on these graphs: for example, car navigation systems search for
the shortest path between two points in a road network, and PageRank can be used on the web graph to
determine the popularity of a web page and thus its ranking in search results. 
In the examples just given, all the vertices in a graph represent the same kind of thing (people, web
pages, or road junctions, respectively). However, graphs are not limited to such homogeneous data:
an equally powerful use of graphs is to provide a consistent way of storing completely different
types of objects in a single datastore. For example, Facebook maintains a single graph with many
different types of vertices and edges: vertices represent people, locations, events, checkins, and
comments made by users; edges indicate which people are friends with each other, which checkin
happened in which location, who commented on which post, who attended which event, and so on
[[35](ch02.html#Bronson2013ud)].