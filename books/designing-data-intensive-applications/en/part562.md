##### TCP Versus UDP 
Some latency-sensitive applications, such as videoconferencing and Voice over IP (VoIP), use UDP
rather than TCP. It’s a trade-off between reliability and variability of delays: as UDP does not
perform flow control and does not retransmit lost packets, it avoids some of the reasons for
variable network delays (although it is still susceptible to switch queues and scheduling delays). UDP is a good choice in situations where delayed data is worthless. For example, in a VoIP phone
call, there probably isn’t enough time to retransmit a lost packet before its data is due to be
played over the loudspeakers. In this case, there’s no point in retransmitting the packet—the
application must instead fill the missing packet’s time slot with silence (causing a brief
interruption in the sound) and move on in the stream. The retry happens at the human layer instead.
(“Could you repeat that please? The sound just cut out for a moment.”)