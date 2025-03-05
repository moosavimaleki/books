However, this is a very weak guarantee—it doesn’t say anything about when the replicas will
converge. Until the time of convergence, reads could return anything or nothing
[[1](ch09.html#Bailis2013jc_ch9)]. For example, if you write a value and
then immediately read it again, there is no guarantee that you will see the value you just wrote,
because the read may be routed to a different replica (see [“Reading Your Own Writes”](ch05.html#sec_replication_ryw)). Eventual consistency is hard for application developers because it is so different from the behavior
of variables in a normal single-threaded program. If you assign a value to a variable and then read
it shortly afterward, you don’t expect to read back the old value, or for the read to fail. A
database looks superficially like a variable that you can read and write, but in fact it has much
more complicated semantics [[3](ch09.html#Scotti2015uc)]. When working with a database that provides only weak guarantees, you need to be constantly aware of
its limitations and not accidentally assume too much. Bugs are often subtle and hard to find by
testing, because the application may work well most of the time. The edge cases of eventual
consistency only become apparent when there is a fault in the system (e.g., a network interruption)
or at high concurrency.