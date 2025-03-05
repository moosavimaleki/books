
The usual way of handling this issue is a timeout: after some time you give up waiting and assume that
the response is not going to arrive. However, when a timeout occurs, you still don’t know whether
the remote node got your request or not (and if the request is still queued somewhere, it may still
be delivered to the recipient, even if the sender has given up on it). ## Network Faults in Practice 
We have been building computer networks for decades—one might hope that by now we would have
figured out how to make them reliable. However, it seems that we have not yet succeeded. 
There are some systematic studies, and plenty of anecdotal evidence, showing that network problems
can be surprisingly common, even in controlled environments like a datacenter operated by one
company [[14](ch08.html#Bailis2014jx)].
One study in a medium-sized datacenter found about 12 network faults per month, of which half
disconnected a single machine, and half disconnected an entire rack
[[15](ch08.html#Leners2015gv)].
Another study measured the failure rates of components like top-of-rack switches, aggregation
switches, and load balancers
[[16](ch08.html#Gill2011ku)].
It found that adding redundant networking gear doesn’t reduce faults as much as you might hope, since it
doesn’t guard against human error (e.g., misconfigured switches), which is a major cause of outages.