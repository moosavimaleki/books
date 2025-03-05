*  Full-text search is arguably a kind of data model that is frequently used alongside databases.
Information retrieval is a large specialist subject that we won’t cover in great detail in this
book, but we’ll touch on search indexes in [Chapter 3](ch03.html#ch_storage) and [Part III](part03.html#part_systems). We have to leave it there for now. In the next chapter we will discuss some of the trade-offs that
come into play when implementing the data models described in this chapter. ##### Footnotes [i](ch02.html#idm140605782666416-marker) A term borrowed from
electronics. Every electric circuit has a certain impedance (resistance to alternating current) on
its inputs and outputs. When you connect one circuit’s output to another one’s input, the power
transfer across the connection is maximized if the output and input impedances of the two circuits
match. An impedance mismatch can lead to signal reflections and other troubles. [ii](ch02.html#idm140605782451264-marker) Literature on the relational model
distinguishes several different normal forms, but the distinctions are of little practical interest.
As a rule of thumb, if you’re duplicating values that could be stored in just one place, the schema
is not normalized.