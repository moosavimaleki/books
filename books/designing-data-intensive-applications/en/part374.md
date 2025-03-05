For defining concurrency, exact time doesn’t matter: we simply call two operations concurrent if
they are both unaware of each other, regardless of the physical time at which they occurred. People
sometimes make a connection between this principle and the special theory of relativity in physics
[[54](ch05.html#Lamport1978jq_ch5)], which introduced the idea that
information cannot travel faster than the speed of light. Consequently, two events that occur some
distance apart cannot possibly affect each other if the time between the events is shorter than the
time it takes light to travel the distance between them. In computer systems, two operations might be concurrent even though the speed of light would in
principle have allowed one operation to affect the other. For example, if the network was slow or
interrupted at the time, two operations can occur some time apart and still be concurrent, because
the network problems prevented one operation from being able to know about the other.