
The design of IMS used a fairly simple data model called the hierarchical model, which has some
remarkable similarities to the JSON model used by document databases
[[2](ch02.html#Stonebraker2005wv)]. It represented all data as a tree
of records nested within records, much like the JSON structure of [Figure 2-2](#fig_json_tree). Like document databases, IMS worked well for one-to-many relationships, but it made many-to-many
relationships difficult, and it didn’t support joins. Developers had to decide whether to duplicate
(denormalize) data or to manually resolve references from one record to another. These problems of
the 1960s and ’70s were very much like the problems that developers are running into with document databases
today [[15](ch02.html#Mei2013vz)]. Various solutions were proposed to solve the limitations of the hierarchical model. The two most
prominent were the relational model (which became SQL, and took over the world) and the network
model (which initially had a large following but eventually faded into obscurity). The “great
debate” between these two camps lasted for much of the 1970s
[[2](ch02.html#Stonebraker2005wv)].