Causality imposes an ordering on events: cause comes before effect; a message is sent before that
message is received; the question comes before the answer. And, like in real life, one thing leads
to another: one node reads some data and then writes something as a result, another node reads the
thing that was written and writes something else in turn, and so on. These chains of causally
dependent operations define the causal order in the system—i.e., what happened before what. If a system obeys the ordering imposed by causality, we say that it is causally consistent. For
example, snapshot isolation provides causal consistency: when you read from the database, and you
see some piece of data, then you must also be able to see any data that causally precedes it
(assuming it has not been deleted in the meantime). ### The causal order is not a total order 
A total order allows any two elements to be compared, so if you have two elements, you can always
say which one is greater and which one is smaller. For example, natural numbers are totally ordered:
if I give you any two numbers, say 5 and 13, you can tell me that 13 is greater than 5.