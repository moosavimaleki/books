This makes the median a good metric if you want to know how long users typically have to wait: half
of user requests are served in less than the median response time, and the other half take longer
than the median. The median is also known as the 50th percentile, and sometimes abbreviated as p50.
Note that the median refers to a single request; if the user makes several requests
(over the course of a session, or because several resources are included in a single page), the
probability that at least one of them is slower than the median is much greater than 50%. In order to figure out how bad your outliers are, you can look at higher percentiles: the 95th,
99th, and 99.9th percentiles are common (abbreviated p95, p99, and p999). They are the
response time thresholds at which 95%, 99%, or 99.9% of requests are faster than that particular
threshold. For example, if the 95th percentile response time is 1.5 seconds, that means 95 out of
100 requests take less than 1.5 seconds, and 5 out of 100 requests take 1.5 seconds or more. This is
illustrated in [Figure 1-4](#fig_lognormal).