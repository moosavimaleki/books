![ddia 0308](assets/ddia_0308.png) ###### Figure 3-8. Simplified outline of ETL into a data warehouse. Data warehouses now exist in almost all large enterprises, but in small companies they are almost
unheard of. This is probably because most small companies don’t have so many different OLTP systems,
and most small companies have a small amount of data—small enough that it can be queried in a
conventional SQL database, or even analyzed in a spreadsheet. In a large company, a lot of heavy
lifting is required to do something that is simple in a small company. A big advantage of using a separate data warehouse, rather than querying OLTP systems directly for
analytics, is that the data warehouse can be optimized for analytic access patterns. It turns out
that the indexing algorithms discussed in the first half of this chapter work well for OLTP, but are
not very good at answering analytic queries. In the rest of this chapter we will look at storage
engines that are optimized for analytics instead.