
In some ways, services are similar to databases: they typically allow clients to submit and query
data. However, while databases allow arbitrary queries using the query languages we discussed in
[Chapter 2](ch02.html#ch_datamodels), services expose an application-specific API that only allows inputs and outputs
that are predetermined by the business logic (application code) of the service
[[33](ch04.html#Helland2005tc_ch4)]. This restriction provides a degree of encapsulation: services can impose
fine-grained restrictions on what clients can and cannot do. A key design goal of a service-oriented/microservices architecture is to make the application easier
to change and maintain by making services independently deployable and evolvable. For example, each
service should be owned by one team, and that team should be able to release new versions of the
service frequently, without having to coordinate with other teams. In other words, we should expect
old and new versions of servers and clients to be running at the same time, and so the data encoding
used by servers and clients must be compatible across versions of the service API—precisely what
we’ve been talking about in this chapter.