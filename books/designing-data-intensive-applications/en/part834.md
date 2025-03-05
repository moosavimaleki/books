
In the case of database queries, we distinguished transaction processing (OLTP) purposes from
analytic purposes (see [“Transaction Processing or Analytics?”](ch03.html#sec_storage_analytics)). We saw that OLTP queries generally look up a
small number of records by key, using indexes, in order to present them to a user (for example, on a
web page). On the other hand, analytic queries often scan over a large number of records, performing
groupings and aggregations, and the output often has the form of a report: a graph showing the
change in a metric over time, or the top 10 items according to some ranking, or a breakdown of some
quantity into subcategories. The consumer of such a report is often an analyst or a manager who
needs to make business decisions. Where does batch processing fit in? It is not transaction processing, nor is it analytics. It is
closer to analytics, in that a batch process typically scans over large portions of an input
dataset. However, a workflow of MapReduce jobs is not the same as a SQL query used for analytic
purposes (see [“Comparing Hadoop to Distributed Databases”](#sec_batch_mr_vs_db)). The output of a batch process is often not a report, but some
other kind of structure.