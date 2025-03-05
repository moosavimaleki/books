1.  Document databases target use cases where data comes in self-contained documents and
relationships between one document and another are rare. 2.  Graph databases go in the opposite direction, targeting use cases where anything is potentially
related to everything. All three models (document, relational, and graph) are widely used today, and each is good in its
respective domain. One model can be emulated in terms of another model—for example, graph data can
be represented in a relational database—but the result is often awkward. That’s why we have
different systems for different purposes, not a single one-size-fits-all solution. One thing that document and graph databases have in common is that they typically don’t enforce a
schema for the data they store, which can make it easier to adapt applications to changing
requirements. However, your application most likely still assumes that data has a certain structure;
it’s just a question of whether the schema is explicit (enforced on write) or implicit (handled on
read).