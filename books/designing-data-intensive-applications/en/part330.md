## Consistent Prefix Reads 
Our third example of replication lag anomalies concerns violation of causality. Imagine the
following short dialog between Mr. Poons and Mrs. Cake: Mr. Poons How far into the future can you see, Mrs. Cake? Mrs. Cake About ten seconds usually, Mr. Poons. There is a causal dependency between those two sentences: Mrs. Cake heard Mr. Poons’s question and
answered it. Now, imagine a third person is listening to this conversation through followers. The things said by
Mrs. Cake go through a follower with little lag, but the things said by Mr. Poons have a longer
replication lag (see [Figure 5-5](#fig_replication_consistent_prefix)). This observer would hear the following: Mrs. Cake About ten seconds usually, Mr. Poons. Mr. Poons How far into the future can you see, Mrs. Cake? To the observer it looks as though Mrs. Cake is answering the question before Mr. Poons has even asked
it. Such psychic powers are impressive, but very confusing
[[25](ch05.html#Pratchett1991wj)].