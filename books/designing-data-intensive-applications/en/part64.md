
An application has to meet various requirements in order to be useful. There are functional
requirements (what it should do, such as allowing data to be stored, retrieved, searched, and processed in
various ways), and some nonfunctional requirements (general properties like security,
reliability, compliance, scalability, compatibility, and maintainability). In this chapter we
discussed reliability, scalability, and maintainability in detail. Reliability means making systems work correctly, even when faults occur. Faults can be in hardware
(typically random and uncorrelated), software (bugs are typically systematic and hard to deal with),
and humans (who inevitably make mistakes from time to time). Fault-tolerance techniques can hide
certain types of faults from the end user. Scalability means having strategies for keeping performance good, even when load increases. In
order to discuss scalability, we first need ways of describing load and performance quantitatively.
We briefly looked at Twitter’s home timelines as an example of describing load, and response time
percentiles as a way of measuring performance. In a scalable system, you can add processing capacity
in order to remain reliable under high load.