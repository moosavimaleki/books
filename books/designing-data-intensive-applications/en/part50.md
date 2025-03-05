
For example, percentiles are often used in service level objectives (SLOs) and service level
agreements (SLAs), contracts that define the expected performance and availability of a service.
An SLA may state that the service is considered to be up if it has a median response time of less than
200 ms and a 99th percentile under 1 s (if the response time is longer, it might as well
be down), and the service may be required to be up at least 99.9% of the time. These metrics set
expectations for clients of the service and allow customers to demand a refund if the SLA is not
met. 
Queueing delays often account for a large part of the response time at high percentiles. As a server can
only process a small number of things in parallel (limited, for example, by its number of CPU cores),
it only takes a small number of slow requests to hold up the processing of subsequent requests—an
effect sometimes known as head-of-line blocking. Even if those subsequent requests are fast to
process on the server, the client will see a slow overall response time due to the time waiting for
the prior request to complete. Due to this effect, it is important to measure response times on the
client side.