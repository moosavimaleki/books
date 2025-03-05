The map function would be called once for each document, resulting in
emit("1995-12", 3) and
emit("1995-12", 4). Subsequently, the reduce function
would be called with reduce("1995-12", [3, 4]), returning
7. 
The map and reduce functions are somewhat restricted in what they are allowed to do. They must be
pure functions, which means they only use the data that is passed to them as input, they cannot
perform additional database queries, and they must not have any side effects. These restrictions
allow the database to run the functions anywhere, in any order, and rerun them on failure. However,
they are nevertheless powerful: they can parse strings, call library functions, perform calculations,
and more. 
MapReduce is a fairly low-level programming model for distributed execution on a cluster of
machines. Higher-level query languages like SQL can be implemented as a pipeline of MapReduce
operations (see [Chapter 10](ch10.html#ch_batch)), but there are also many distributed implementations of SQL that don’t
use MapReduce. Note there is nothing in SQL that constrains it to running on a single machine, and
MapReduce doesn’t have a monopoly on distributed query execution.