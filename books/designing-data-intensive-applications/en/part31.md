
The things that can go wrong are called faults, and systems that anticipate faults and can cope
with them are called fault-tolerant or resilient. The former term is slightly misleading: it
suggests that we could make a system tolerant of every possible kind of fault, which in reality is
not feasible.  If the entire planet Earth (and all servers on it) were
swallowed by a black hole, tolerance of that fault would require web hosting in space—good luck
getting that budget item approved. So it only makes sense to talk about tolerating certain types
of faults. 
Note that a fault is not the same as a failure
[[2](ch01.html#Heimerdinger1992vn)]. A fault is usually defined as one component of the system
deviating from its spec, whereas a failure is when the system as a whole stops providing the
required service to the user. It is impossible to reduce the probability of a fault to zero;
therefore it is usually best to design fault-tolerance mechanisms that prevent faults from causing
failures. In this book we cover several techniques for building reliable systems from unreliable
parts.