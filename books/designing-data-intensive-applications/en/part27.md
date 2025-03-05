So why should we lump them all together under an umbrella term like data systems? Many new tools for data storage and processing have emerged in recent years. They are optimized for
a variety of different use cases, and they no longer neatly fit into traditional categories
[[1](ch01.html#Stonebraker2005ux)]. 
For example, there are datastores that are also used as message queues (Redis), and there are
message queues with database-like durability guarantees (Apache Kafka). The boundaries between the
categories are becoming blurred. Secondly, increasingly many applications now have such demanding or wide-ranging requirements that a
single tool can no longer meet all of its data processing and storage needs. Instead, the work is
broken down into tasks that can be performed efficiently on a single tool, and those different
tools are stitched together using application code. 
For example, if you have an application-managed caching layer (using Memcached or similar), or a
full-text search server (such as Elasticsearch or Solr) separate from your main database, it is
normally the application code’s responsibility to keep those caches and indexes in sync with the
main database. [Figure 1-1](#fig_introduction_composite) gives a glimpse of what this may look like (we will
go into detail in later chapters).