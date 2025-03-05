An advantage of distinguishing between safety and liveness properties is that it helps us deal with
difficult system models. For distributed algorithms, it is common to require that safety properties
always hold, in all possible situations of a system model
[[88](ch08.html#Dwork1988dr_ch8)]. That is, even if all nodes crash, or
the entire network fails, the algorithm must nevertheless ensure that it does not return a wrong
result (i.e., that the safety properties remain satisfied). However, with liveness properties we are allowed to make caveats: for example, we could say that a
request needs to receive a response only if a majority of nodes have not crashed, and only if the
network eventually recovers from an outage. The definition of the partially synchronous model
requires that eventually the system returns to a synchronous state—that is, any period of network
interruption lasts only for a finite duration and is then repaired. ### Mapping system models to the real world