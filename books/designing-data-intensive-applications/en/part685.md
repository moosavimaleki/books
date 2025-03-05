### Linearizability is stronger than causal consistency 
So what is the relationship between the causal order and linearizability? The answer is that
linearizability implies causality: any system that is linearizable will preserve causality
correctly [[7](ch09.html#Lamport1986cg)]. In particular, if there are
multiple communication channels in a system (such as the message queue and the file storage service
in [Figure 9-5](#fig_consistency_thumbnailer)), linearizability ensures that causality is automatically
preserved without the system having to do anything special (such as passing around timestamps
between different components). The fact that linearizability ensures causality is what makes linearizable systems simple to
understand and appealing. However, as discussed in [“The Cost of Linearizability”](#sec_linearizability_cost), making a system
linearizable can harm its performance and availability, especially if the system has significant
network delays (for example, if it’s geographically distributed). For this reason, some distributed
data systems have abandoned linearizability, which allows them to achieve better performance but can
make them difficult to work with.