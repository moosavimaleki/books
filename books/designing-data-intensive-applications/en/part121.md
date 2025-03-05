But equivalently, you could start with the two Location vertices and work backward. If there is
an index on the name property, you can probably efficiently find the two vertices representing the
US and Europe. Then you can proceed to find all locations (states, regions, cities, etc.) in the US
and Europe respectively by following all incoming WITHIN edges. Finally, you can look for people
who can be found through an incoming BORN_IN or LIVES_IN edge at one of the location vertices. As is typical for a declarative query language, you don’t need to specify such execution details when
writing the query: the query optimizer automatically chooses the strategy that is predicted to be
the most efficient, so you can get on with writing the rest of your application. ## Graph Queries in SQL [Example 2-2](#fig_graph_sql_schema) suggested that graph data can be represented in a relational database. But
if we put graph data in a relational structure, can we also query it using SQL?