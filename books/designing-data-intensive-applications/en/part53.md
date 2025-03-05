![ddia 0105](assets/ddia_0105.png) ###### Figure 1-5. When several backend calls are needed to serve a request, it takes just a single slow backend request to slow down the entire end-user request. ## Approaches for Coping with Load 
Now that we have discussed the parameters for describing load and metrics for measuring
performance, we can start discussing scalability in earnest: how do we maintain good performance
even when our load parameters increase by some amount? An architecture that is appropriate for one level of load is unlikely to cope with 10 times that
load. If you are working on a fast-growing service, it is therefore likely that you will need to
rethink your architecture on every order of magnitude load increase—or perhaps even more often than
that. 
People often talk of a dichotomy between scaling up (vertical scaling, moving to a more powerful
machine) and scaling out (horizontal scaling, distributing the load across multiple smaller
machines). Distributing load across multiple machines is also known as a shared-nothing
architecture. A system that can run on a single machine is often simpler, but high-end machines can
become very expensive, so very intensive workloads often can’t avoid scaling out. In reality, good
architectures usually involve a pragmatic mixture of approaches: for example, using several fairly
powerful machines can still be simpler and cheaper than a large number of small virtual machines.