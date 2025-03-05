### Capturing causal dependencies 
We won’t go into all the nitty-gritty details of how nonlinearizable systems can maintain causal
consistency here, but just briefly explore some of the key ideas. In order to maintain causality, you need to know which operation happened before which other
operation. This is a partial order: concurrent operations may be processed in any order, but if one
operation happened before another, then they must be processed in that order on every replica. Thus,
when a replica processes an operation, it must ensure that all causally preceding operations (all
operations that happened before) have already been processed; if some preceding operation is
missing, the later operation must wait until the preceding operation has been processed. In order to determine causal dependencies, we need some way of describing the “knowledge” of a node
in the system. If a node had already seen the value X when it issued the write Y, then X and Y may
be causally related. The analysis uses the kinds of questions you would expect in a
criminal investigation of fraud charges: did the CEO know about X at the time when they made
decision Y?