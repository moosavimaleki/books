# Part III. Derived Data

# Part III. Derived Data In Parts [I](part01.html#part_foundations)
and [II](part02.html#part_distributed_data)
of this book, we assembled from the ground up all the major considerations that go into a
distributed database, from the layout of data on disk all the way to the limits of distributed
consistency in the presence of faults. However, this discussion assumed that there was only one
database in the application. In reality, data systems are often more complex. In a large application you often need to be able to
access and process data in many different ways, and there is no one database that can satisfy all
those different needs simultaneously. Applications thus commonly use a combination of several
different datastores, indexes, caches, analytics systems, etc. and implement mechanisms for moving
data from one store to another. 
In this final part of the book, we will examine the issues around integrating multiple
different data systems, potentially with different data models and optimized for different access
patterns, into one coherent application architecture. This aspect of system-building is often
overlooked by vendors who claim that their product can satisfy all your needs. In reality,
integrating disparate systems is one of the most important things that needs to be done in a
nontrivial application.