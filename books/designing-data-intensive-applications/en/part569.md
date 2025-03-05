By contrast, the internet shares network bandwidth dynamically. Senders push and jostle with each
other to get their packets over the wire as quickly as possible, and the network switches decide
which packet to send (i.e., the bandwidth allocation) from one moment to the next. This approach has the
downside of queueing, but the advantage is that it maximizes utilization of the wire. The wire has a
fixed cost, so if you utilize it better, each byte you send over the wire is cheaper. 
A similar situation arises with CPUs: if you share each CPU core dynamically between several
threads, one thread sometimes has to wait in the operating system’s run queue while another thread
is running, so a thread can be paused for varying lengths of time. However, this utilizes the
hardware better than if you allocated a static number of CPU cycles to each thread (see
[“Response time guarantees”](#sec_distributed_clocks_realtime)). Better hardware utilization is also a significant motivation
for using virtual machines.