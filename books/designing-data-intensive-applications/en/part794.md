[![5](assets/5.png)](#co_batch_processing_CO2-5) Print out those top five entries. This program is not as concise as the chain of Unix pipes, but it’s fairly readable, and which of
the two you prefer is partly a matter of taste. However, besides the superficial syntactic
differences between the two, there is a big difference in the execution flow, which becomes apparent
if you run this analysis on a large file. ### Sorting versus in-memory aggregation The Ruby script keeps an in-memory hash table of URLs, where each URL is mapped to the number of
times it has been seen. The Unix pipeline example does not have such a hash table, but instead
relies on sorting a list of URLs in which multiple occurrences of the same URL are simply repeated. 
Which approach is better? It depends how many different URLs you have. For most small to mid-sized
websites, you can probably fit all distinct URLs, and a counter for each URL, in (say) 1 GB of
memory. In this example, the working set of the job (the amount of memory to which the job needs
random access) depends only on the number of distinct URLs: if there are a million log entries for a
single URL, the space required in the hash table is still just one URL plus the size of the counter.
If this working set is small enough, an in-memory hash table works fine—even on a laptop.