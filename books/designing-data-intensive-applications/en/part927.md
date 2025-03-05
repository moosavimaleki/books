
However, dual writes have some serious problems, one of which is a race condition illustrated in
[Figure 11-4](#fig_stream_write_order). In this example, two clients concurrently want to update an item X:
client 1 wants to set the value to A, and client 2 wants to set it to B. Both clients first write
the new value to the database, then write it to the search index. Due to unlucky timing, the
requests are interleaved: the database first sees the write from client 1 setting the value to A,
then the write from client 2 setting the value to B, so the final value in the database is B. The
search index first sees the write from client 2, then client 1, so the final value in the search
index is A. The two systems are now permanently inconsistent with each other, even though no error
occurred. ![ddia 1104](assets/ddia_1104.png) ###### Figure 11-4. In the database, X is first set to A and then to B, while at the search index the writes arrive in the opposite order.