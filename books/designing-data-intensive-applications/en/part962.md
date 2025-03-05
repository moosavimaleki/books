
For example, media monitoring services subscribe to feeds of news articles and broadcasts from media
outlets, and search for any news mentioning companies, products, or topics of interest. This is done
by formulating a search query in advance, and then continually matching the stream of news items
against this query. Similar features exist on some websites: for example, users of real estate
websites can ask to be notified when a new property matching their search criteria appears on the
market. The percolator feature of Elasticsearch
[[76](ch11.html#Banon2011hw)] is one option for implementing this kind of stream search. Conventional search engines first index the documents and then run queries over the index. By
contrast, searching a stream turns the processing on its head: the queries are stored, and the
documents run past the queries, like in CEP. In the simplest case, you can test every document
against every query, although this can get slow if you have a large number of queries. To optimize
the process, it is possible to index the queries as well as the documents, and thus narrow down the
set of queries that may match
[[77](ch11.html#Woodward2015vy)].