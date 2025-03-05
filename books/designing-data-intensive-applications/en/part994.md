[iii](ch11.html#idm140605756368864-marker) If you regard a stream as the derivative
of a table, as in [Figure 11-6](#fig_stream_integral), and regard a join as a product
of two tables u·v, something interesting happens: the stream of changes to the
materialized join follows the product rule
(u·v)′ = u′v + uv′.
In words: any change of tweets is joined with the current followers, and any change of followers is
joined with the current tweets [[49](ch11.html#Hyde2016),
[50](ch11.html#Gupta1999uz)]. ##### References [[1](ch11.html#Akidau2015gh-marker)] Tyler Akidau, Robert Bradshaw, Craig Chambers, et al.:
“[The Dataflow Model: A Practical Approach to
Balancing Correctness, Latency, and Cost in Massive-Scale, Unbounded, Out-of-Order Data Processing](http://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf),”
Proceedings of the VLDB Endowment, volume 8, number 12, pages 1792–1803, August 2015.
[doi:10.14778/2824032.2824076](http://dx.doi.org/10.14778/2824032.2824076) [[2](ch11.html#Abelson1996ut-marker)] Harold Abelson, Gerald Jay Sussman, and Julie Sussman:
[Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sicp/),
2nd edition. MIT Press, 1996. ISBN: 978-0-262-51087-5, available online at mitpress.mit.edu [[3](ch11.html#Eugster2003ih_ch11-marker)] Patrick Th. Eugster, Pascal A. Felber,
Rachid Guerraoui, and Anne-Marie Kermarrec:
“[The Many Faces of Publish/Subscribe](http://www.cs.ru.nl/~pieter/oss/manyfaces.pdf),”
ACM Computing Surveys, volume 35, number 2, pages 114–131, June 2003.
[doi:10.1145/857076.857078](http://dx.doi.org/10.1145/857076.857078)