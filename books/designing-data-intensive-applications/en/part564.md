
Even better, rather than using configured constant timeouts, systems can continually measure
response times and their variability (jitter), and automatically adjust timeouts according to the
observed response time distribution. This can be done with a Phi Accrual failure detector
[[30](ch08.html#Hayashibara2004vw)],
which is used for example in Akka and Cassandra [[31](ch08.html#Wang2013wa)].
TCP retransmission timeouts also work similarly
[[27](ch08.html#Jacobson1988gl)]. ## Synchronous Versus Asynchronous Networks 
Distributed systems would be a lot simpler if we could rely on the network to deliver packets with
some fixed maximum delay, and not to drop packets. Why can’t we solve this at the hardware level
and make the network reliable so that the software doesn’t need to worry about it? To answer this question, it’s interesting to compare datacenter networks to the traditional fixed-line
telephone network (non-cellular, non-VoIP), which is extremely reliable: delayed audio
frames and dropped calls are very rare. A phone call requires a constantly low end-to-end latency
and enough bandwidth to transfer the audio samples of your voice. Wouldn’t it be nice to have
similar reliability and predictability in computer networks?