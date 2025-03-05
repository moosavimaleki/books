It’s quite repetitive to repeat the same subject over and over again, but fortunately you can use
semicolons to say multiple things about the same subject. This makes the Turtle format quite nice
and readable: see [Example 2-7](#fig_graph_n3_shorthand). ##### Example 2-7. A more concise way of writing the data in [Example 2-6](#fig_graph_n3_triples) ```
@prefix : .
_:lucy     a :Person;   :name "Lucy";          :bornIn _:idaho.
_:idaho    a :Location; :name "Idaho";         :type "state";   :within _:usa.
_:usa      a :Location; :name "United States"; :type "country"; :within _:namerica.
_:namerica a :Location; :name "North America"; :type "continent".
``` ### The semantic web 
If you read more about triple-stores, you may get sucked into a maelstrom of articles written about
the semantic web. The triple-store data model is completely independent of the semantic web—for
example, Datomic
[[40](ch02.html#Datomic2013)]
is a triple-store that does not claim to have anything to do with
it.[vii](ch02.html#idm140605780363744)
But since the two are so closely linked in many people’s minds, we should discuss them briefly.