### Building search indexes 
Google’s original use of MapReduce was to build indexes for its search engine, which was
implemented as a workflow of 5 to 10 MapReduce jobs
[[1](ch10.html#Dean2004ua_ch10)].
Although Google later moved away from using MapReduce for this purpose
[[43](ch10.html#Peng2010ub)],
it helps to understand MapReduce if you look at it through the lens of building a search index.
(Even today, Hadoop MapReduce remains a good way of building indexes for Lucene/Solr
[[44](ch10.html#ClouderaSearch)].) We saw briefly in [“Full-text search and fuzzy indexes”](ch03.html#sec_storage_full_text) how a full-text search index such as Lucene works: it is
a file (the term dictionary) in which you can efficiently look up a particular keyword and find the
list of all the document IDs containing that keyword (the postings list). This is a very simplified
view of a search index—in reality it requires various additional data, in order to rank search
results by relevance, correct misspellings, resolve synonyms, and so on—but the principle holds.