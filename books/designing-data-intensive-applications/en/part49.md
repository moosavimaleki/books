
High percentiles of response times, also known as tail latencies, are important because they
directly affect users’ experience of the service. For example, Amazon describes response time
requirements for internal services in terms of the 99.9th percentile, even though it only affects 1
in 1,000 requests. This is because the customers with the slowest requests are often those who have
the most data on their accounts because they have made many purchases—that is, they’re the most
valuable customers
[[19](ch01.html#DeCandia2007ui_ch1)].
It’s important to keep those customers happy by ensuring the website is fast for them: Amazon has
also observed that a 100 ms increase in response time reduces sales by 1%
[[20](ch01.html#MakeDataUseful2006td)],
and others report that a 1-second slowdown reduces a customer satisfaction metric by 16%
[[21](ch01.html#Everts2014vm),
[22](ch01.html#Brutlag2009ut)]. On the other hand, optimizing the 99.99th percentile (the slowest 1 in 10,000 requests) was deemed
too expensive and to not yield enough benefit for Amazon’s purposes. Reducing response times at very
high percentiles is difficult because they are easily affected by random events outside of your
control, and the benefits are diminishing.