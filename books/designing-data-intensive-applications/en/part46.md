Even if you only make the same request over and over again, you’ll get a slightly different response
time on every try. In practice, in a system handling a variety of requests, the response time can
vary a lot. We therefore need to think of response time not as a single number, but as a
distribution of values that you can measure. 
In [Figure 1-4](#fig_lognormal), each gray bar represents a request to a service, and its height shows how long
that request took. Most requests are reasonably fast, but there are occasional outliers that take
much longer. Perhaps the slow requests are intrinsically more expensive, e.g., because they process
more data. But even in a scenario where you’d think all requests should take the same time, you get
variation: random additional latency could be introduced by a context switch to a background
process, the loss of a network packet and TCP retransmission, a garbage collection pause, a page
fault forcing a read from disk, mechanical vibrations in the server rack
[[18](ch01.html#Sommers2014va)],
or many other causes.