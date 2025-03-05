In the simplest case, an access path could be like the traversal of a linked list: start at the head
of the list, and look at one record at a time until you find the one you want. But in a world of
many-to-many relationships, several different paths can lead to the same record, and a programmer
working with the network model had to keep track of these different access paths in their head. A query in CODASYL was performed by moving a cursor through the database by iterating over lists of
records and following access paths. If a record had multiple parents (i.e., multiple incoming
pointers from other records), the application code had to keep track of all the various
relationships. Even CODASYL committee members admitted that this was like navigating around an
n-dimensional data space [[17](ch02.html#Bachman1973hs)]. Although manual access path selection was able to make the most efficient use of the very limited
hardware capabilities in the 1970s (such as tape drives, whose seeks are extremely slow), the
problem was that they made the code for querying and updating the database complicated and
inflexible. With both the hierarchical and the network model, if you didn’t have a path to the data
you wanted, you were in a difficult situation. You could change the access paths, but then you had
to go through a lot of handwritten database query code and rewrite it to handle the new access
paths. It was difficult to make changes to an application’s data model.