
If you want to add response time percentiles to the monitoring dashboards for your services, you
need to efficiently calculate them on an ongoing basis. For example, you may want to keep a rolling
window of response times of requests in the last 10 minutes. Every minute, you calculate the median
and various percentiles over the values in that window and plot those metrics on a graph. 
The naïve implementation is to keep a list of response times for all requests within the time
window and to sort that list every minute. If that is too inefficient for you, there are algorithms
that can calculate a good approximation of percentiles at minimal CPU and memory cost, such as
forward decay [[25](ch01.html#Cormode2009vz)], t-digest
[[26](ch01.html#Dunning2014wm)], or HdrHistogram
[[27](ch01.html#HdrHistogram)].
Beware that averaging percentiles, e.g., to reduce the time resolution or to combine data from
several machines, is mathematically meaningless—the right way of aggregating response time data
is to add the histograms [[28](ch01.html#Schwartz2015tg)].