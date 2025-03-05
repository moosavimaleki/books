Those features give graphs a great deal of flexibility for data modeling, as illustrated in
[Figure 2-5](#fig_datamodels_graph). The figure shows a few things that would be difficult to express in a
traditional relational schema, such as different kinds of regional structures in different countries
(France has départements and régions, whereas the US has counties and states), quirks of
history such as a country within a country (ignoring for now the intricacies of sovereign states and
nations), and varying granularity of data (Lucy’s current residence is specified as a city, whereas
her place of birth is specified only at the level of a state). You could imagine extending the graph to also include many other facts about Lucy and Alain, or
other people. For instance, you could use it to indicate any food allergies they have (by
introducing a vertex for each allergen, and an edge between a person and an allergen to indicate an
allergy), and link the allergens with a set of vertices that show which foods contain which
substances. Then you could write a query to find out what is safe for each person to eat.

Graphs are good for evolvability: as you add features to your application, a graph can easily be
extended to accommodate changes in your application’s data structures.