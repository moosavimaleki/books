##### Footnotes [i](ch03.html#idm140605778351696-marker) If all keys and
values had a fixed size, you could use binary search on a segment file and avoid the in-memory
index entirely. However, they are usually variable-length in practice, which makes it difficult to
tell where one record ends and the next one starts if you don’t have an index. [ii](ch03.html#idm140605778235856-marker) Inserting a new
key into a B-tree is reasonably intuitive, but deleting one (while keeping the tree balanced) is
somewhat more involved [[2](ch03.html#Cormen2009uw)]. [iii](ch03.html#idm140605778198240-marker) This variant is
sometimes known as a B+ tree, although the optimization is so common
that it often isn’t distinguished from other B-tree variants. [iv](ch03.html#idm140605777918240-marker) The meaning of online
in OLAP is unclear; it probably refers to the fact that queries are not just for predefined reports,
but that analysts use the OLAP system interactively for explorative queries. ##### References [[1](ch03.html#Aho1983vj-marker)] Alfred V. Aho, John E. Hopcroft, and Jeffrey D. Ullman:
Data Structures and Algorithms. Addison-Wesley, 1983. ISBN: 978-0-201-00023-8