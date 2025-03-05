# Chapter 9. Consistency and Consensus

# Chapter 9. Consistency and Consensus Is it better to be alive and wrong or right and dead? Jay Kreps, A Few Notes on Kafka and Jepsen (2013) ![](assets/ch09-map-ebook.png) Lots of things can go wrong in distributed systems, as discussed in [Chapter 8](ch08.html#ch_distributed). The simplest
way of handling such faults is to simply let the entire service fail, and show the user an error
message. If that solution is unacceptable, we need to find ways of tolerating faults—that is, of
keeping the service functioning correctly, even if some internal component is faulty. In this chapter, we will talk about some examples of algorithms and protocols for building
fault-tolerant distributed systems. We will assume that all the problems from [Chapter 8](ch08.html#ch_distributed) can
occur: packets can be lost, reordered, duplicated, or arbitrarily delayed in the network; clocks are
approximate at best; and nodes can pause (e.g., due to garbage collection) or crash at any time.