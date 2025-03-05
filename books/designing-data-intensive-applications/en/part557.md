Rapid feedback about a remote node being down is useful, but you can’t count on it. Even if TCP
acknowledges that a packet was delivered, the application may have crashed before handling it. If
you want to be sure that a request was successful, you need a positive response from the application
itself [[24](ch08.html#Saltzer1984do_ch8)]. Conversely, if something has gone wrong, you may get an error response at some level of the stack,
but in general you have to assume that you will get no response at all. You can retry a few times
(TCP retries transparently, but you may also retry at the application level), wait for a timeout to
elapse, and eventually declare the node dead if you don’t hear back within the timeout. ## Timeouts and Unbounded Delays 
If a timeout is the only sure way of detecting a fault, then how long should the timeout be? There
is unfortunately no simple answer.