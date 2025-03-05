## Graphs and Iterative Processing 
In [“Graph-Like Data Models”](ch02.html#sec_datamodels_graph) we discussed using graphs for modeling data, and using graph query
languages to traverse the edges and vertices in a graph. The discussion in [Chapter 2](ch02.html#ch_datamodels) was
focused around OLTP-style use: quickly executing queries to find a small number of vertices matching
certain criteria. 
It is also interesting to look at graphs in a batch processing context, where the goal is to perform
some kind of offline processing or analysis on an entire graph. This need often arises in machine
learning applications such as recommendation engines, or in ranking systems. For example, one of the
most famous graph analysis algorithms is PageRank
[[69](ch10.html#Page1999wg)],
which tries to estimate the popularity of a web page based on what other web pages link to it. It is
used as part of the formula that determines the order in which web search engines present their
results.