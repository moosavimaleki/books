### Bringing related data together in the same place 
In a sort-merge join, the mappers and the sorting process make sure that all the necessary data to
perform the join operation for a particular user ID is brought together in the same place: a single
call to the reducer. Having lined up all the required data in advance, the reducer can be a fairly
simple, single-threaded piece of code that can churn through records with high throughput and low
memory overhead. One way of looking at this architecture is that mappers “send messages” to the reducers. When a
mapper emits a key-value pair, the key acts like the destination address to which the value should be
delivered. Even though the key is just an arbitrary string (not an actual network address like an
IP address and port number), it behaves like an address: all key-value pairs with the same key will be
delivered to the same destination (a call to the reducer).