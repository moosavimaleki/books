
This is no coincidence: it can be proved that a linearizable compare-and-set (or increment-and-get)
register and total order broadcast are both equivalent to consensus
[[28](ch09.html#Herlihy1991gk),
[67](ch09.html#Chandra1996cp)].
That is, if you can solve one of these problems, you can transform it into a solution for the
others. This is quite a profound and surprising insight! It is time to finally tackle the consensus problem head-on, which we will do in the rest of this
chapter. # Distributed Transactions and Consensus 
Consensus is one of the most important and fundamental problems in distributed computing. On the
surface, it seems simple: informally, the goal is simply to get several nodes to agree on
something. You might think that this shouldn’t be too hard. Unfortunately, many broken systems have
been built in the mistaken belief that this problem is easy to solve. Although consensus is very important, the section about it appears late in this book because the
topic is quite subtle, and appreciating the subtleties requires some prerequisite knowledge. Even
in the academic research community, the understanding of consensus only gradually crystallized over
the course of decades, with many misunderstandings along the way. Now that we have discussed
replication ([Chapter 5](ch05.html#ch_replication)), transactions ([Chapter 7](ch07.html#ch_transactions)), system models
([Chapter 8](ch08.html#ch_distributed)), linearizability, and total order broadcast (this chapter), we are
finally ready to tackle the consensus problem.