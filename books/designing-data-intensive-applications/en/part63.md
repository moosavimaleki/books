
Most discussions of these Agile techniques focus on a fairly small, local scale (a couple of source
code files within the same application). In this book, we search for ways of increasing agility on
the level of a larger data system, perhaps consisting of several different applications or services
with different characteristics. For example, how would you “refactor” Twitter’s architecture for
assembling home timelines ([“Describing Load”](#sec_introduction_scalability_load)) from approach 1 to approach 2? The ease with which you can modify a data system, and adapt it to changing requirements, is closely
linked to its simplicity and its abstractions: simple and easy-to-understand systems are usually
easier to modify than complex ones. But since this is such an important idea, we will use a
different word to refer to agility on a data system level: evolvability
[[34](ch01.html#Breivold2008dm)]. # Summary In this chapter, we have explored some fundamental ways of thinking about data-intensive
applications. These principles will guide us through the rest of the book, where we dive into deep
technical detail.