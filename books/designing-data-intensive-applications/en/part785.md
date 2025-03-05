# Chapter 10. Batch Processing

# Chapter 10. Batch Processing A system cannot be successful if it is too strongly influenced by a single person. Once the initial
design is complete and fairly robust, the real test begins as people with many different viewpoints
undertake their own experiments. Donald Knuth ![](assets/ch10-map.png) 
In the first two parts of this book we talked a lot about requests and queries, and the
corresponding responses or results. This style of data processing is assumed in many modern data
systems: you ask for something, or you send an instruction, and some time later the system
(hopefully) gives you an answer. Databases, caches, search indexes, web servers, and many other
systems work this way. 
In such online systems, whether it’s a web browser requesting a page or a service calling a
remote API, we generally assume that the request is triggered by a human user, and that the user is
waiting for the response. They shouldn’t have to wait too long, so we pay a lot of
attention to the response time of these systems (see [“Describing Performance”](ch01.html#sec_introduction_percentiles)).