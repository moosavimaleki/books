
The idea is similar to a data warehouse (see [“Data Warehousing”](ch03.html#sec_storage_dwh)): simply bringing data from various
parts of a large organization together in one place is valuable, because it enables joins across
datasets that were previously disparate. The careful schema design required by an MPP database slows
down that centralized data collection; collecting data in its raw form, and worrying about schema
design later, allows the data collection to be speeded up (a concept sometimes known as a “data
lake” or “enterprise data hub” [[55](ch10.html#Terrizzano2015tk)]). 
Indiscriminate data dumping shifts the burden of interpreting the data: instead of forcing the
producer of a dataset to bring it into a standardized format, the interpretation of the data becomes
the consumer’s problem (the schema-on-read approach [[56](ch10.html#Roberts2015tl)];
see [“Schema flexibility in the document model”](ch02.html#sec_datamodels_schema_flexibility)).
This can be an advantage if the producer and consumers are different teams with different
priorities. There may not even be one ideal data model, but rather different views onto the data
that are suitable for different purposes. Simply dumping data in its raw form allows for several
such transformations. This approach has been dubbed the sushi principle: “raw data is better”
[[57](ch10.html#Johnson2015ua)].