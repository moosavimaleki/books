
Technically speaking, derived data is redundant, in the sense that it duplicates
existing information. However, it is often essential for getting good performance on read queries.
It is commonly denormalized. You can derive several different datasets from a single
source, enabling you to look at the data from different “points of view.” Not all systems make a clear distinction between systems of record and derived data in their
architecture, but it’s a very helpful distinction to make, because it clarifies the dataflow
through your system: it makes explicit which parts of the system have which inputs and which
outputs, and how they depend on each other. Most databases, storage engines, and query languages are not inherently either a system of record
or a derived system. A database is just a tool: how you use it is up to you. The distinction between
system of record and derived data system depends not on the tool, but on how you use it in your
application.