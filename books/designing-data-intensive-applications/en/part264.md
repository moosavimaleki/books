Schema evolution thus allows the entire database to appear as if it was encoded with a single
schema, even though the underlying storage may contain records encoded with various historical
versions of the schema. ### Archival storage 
Perhaps you take a snapshot of your database from time to time, say for backup purposes or for
loading into a data warehouse (see [“Data Warehousing”](ch03.html#sec_storage_dwh)). In this case, the data dump will typically
be encoded using the latest schema, even if the original encoding in the source database contained a
mixture of schema versions from different eras. Since you’re copying the data anyway, you might as
well encode the copy of the data consistently. 
As the data dump is written in one go and is thereafter immutable, formats like Avro object
container files are a good fit. This is also a good opportunity to encode the data in an
analytics-friendly column-oriented format such as Parquet (see [“Column Compression”](ch03.html#sec_storage_column_compression)).