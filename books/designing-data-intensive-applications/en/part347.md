Other kinds of conflict can be more subtle to detect. For example, consider a meeting room booking
system: it tracks which room is booked by which group of people at which time. This application
needs to ensure that each room is only booked by one group of people at any one time (i.e., there
must not be any overlapping bookings for the same room). In this case, a conflict may arise if two
different bookings are created for the same room at the same time. Even if the application checks
availability before allowing a user to make a booking, there can be a conflict if the two bookings
are made on two different leaders. There isn’t a quick ready-made answer, but in the following chapters we will trace a path toward a
good understanding of this problem. We will see some more examples of conflicts in
[Chapter 7](ch07.html#ch_transactions), and in [Chapter 12](ch12.html#ch_future) we will discuss scalable approaches for detecting and
resolving conflicts in a replicated system.