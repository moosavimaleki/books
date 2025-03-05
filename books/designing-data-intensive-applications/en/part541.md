Working with distributed systems is fundamentally different from writing software on a single
computer—and the main difference is that there are lots of new and exciting ways for things to go
wrong [[1](ch08.html#Cavage2013ez),
[2](ch08.html#Kreps2012td_ch8)].
In this chapter, we will get a taste of the problems that arise in practice, and an understanding of
the things we can and cannot rely on. In the end, our task as engineers is to build systems that do their job (i.e., meet the guarantees
that users are expecting), in spite of everything going wrong. In [Chapter 9](ch09.html#ch_consistency), we will look
at some examples of algorithms that can provide such guarantees in a distributed system. But first,
in this chapter, we must understand what challenges we are up against. This chapter is a thoroughly pessimistic and depressing overview of things that may go wrong in a
distributed system. We will look into problems with networks ([“Unreliable Networks”](#sec_distributed_networks)); clocks
and timing issues ([“Unreliable Clocks”](#sec_distributed_clocks)); and we’ll discuss to what degree they are avoidable.
The consequences of all these issues are disorienting, so
we’ll explore how to think about the state of a distributed system and how to reason about things
that have happened ([“Knowledge, Truth, and Lies”](#sec_distributed_truth)).