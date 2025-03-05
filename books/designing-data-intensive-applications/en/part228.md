# Chapter 4. Encoding and Evolution

# Chapter 4. Encoding and Evolution Everything changes and nothing stands still. Heraclitus of Ephesus, as quoted by Plato in Cratylus (360 BCE) ![](assets/ch04-map-ebook.png) 
Applications inevitably change over time. Features are added or modified as new products are
launched, user requirements become better understood, or business circumstances change. In
[Chapter 1](ch01.html#ch_introduction) we introduced the idea of evolvability: we should aim to build systems that
make it easy to adapt to change (see [“Evolvability: Making Change Easy”](ch01.html#sec_introduction_evolvability)). In most cases, a change to an application’s features also requires a change to data that it stores:
perhaps a new field or record type needs to be captured, or perhaps existing data needs to be
presented in a new way. 
The data models we discussed in [Chapter 2](ch02.html#ch_datamodels) have different ways of coping with such change.
Relational databases generally assume that all data in the database conforms to one schema: although
that schema can be changed (through schema migrations; i.e., ALTER statements), there is exactly
one schema in force at any one point in time. By contrast, schema-on-read (“schemaless”) databases
don’t enforce a schema, so the database can contain a mixture of older and newer data formats
written at different times (see [“Schema flexibility in the document model”](ch02.html#sec_datamodels_schema_flexibility)).