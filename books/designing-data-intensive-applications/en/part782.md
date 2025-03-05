# Systems of Record and Derived Data On a high level, systems that store and process data can be grouped into two broad categories: Systems of record 
    A system of record, also known as source of truth, holds the authoritative version
    of your data.  When new data comes in, e.g., as user input, it is first written here. Each fact
    is represented exactly once (the representation is typically normalized). If there is
    any discrepancy between another system and the system of record, then the value in the system of
    record is (by definition) the correct one. Derived data systems 
    Data in a derived system is the result of taking some existing data from another system and
    transforming or processing it in some way. If you lose derived data, you can recreate it from
    the original source. A classic example is a cache: data can be served from the cache if present,
    but if the cache doesn’t contain what you need, you can fall back to the underlying
    database. Denormalized values, indexes, and materialized views also fall into this category. In
    recommendation systems, predictive summary data is often derived from usage logs.