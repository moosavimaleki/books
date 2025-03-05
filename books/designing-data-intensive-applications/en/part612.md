However, in the kinds of systems we discuss in this book, we can usually safely assume that there
are no Byzantine faults. In your datacenter, all the nodes are controlled by your organization (so
they can hopefully be trusted) and radiation levels are low enough that memory corruption is not a
major problem. Protocols for making systems Byzantine fault-tolerant are quite complicated
[[84](ch08.html#Mickens2013tp)],
and fault-tolerant embedded systems rely on support from the hardware level
[[81](ch08.html#Rushby2001vu)]. In most server-side data systems, the
cost of deploying Byzantine fault-tolerant solutions makes them impractical. 
Web applications do need to expect arbitrary and malicious behavior of clients that are under
end-user control, such as web browsers. This is why input validation, sanitization, and output
escaping are so important: to prevent SQL injection and cross-site scripting, for example. However,
we typically don’t use Byzantine fault-tolerant protocols here, but simply make the server the
authority on deciding what client behavior is and isn’t allowed. In peer-to-peer networks, where
there is no such central authority, Byzantine fault tolerance is more relevant.