Although the system can be more reliable than its underlying parts, there is always a limit to how
much more reliable it can be. For example, error-correcting codes can deal with a small number of
single-bit errors, but if your signal is swamped by interference, there is a fundamental limit to
how much data you can get through your communication channel
[[13](ch08.html#Shannon1948wk)].
TCP can hide packet loss, duplication, and reordering from you, but it cannot magically remove delays
in the network. 
Although the more reliable higher-level system is not perfect, it’s still useful because it takes
care of some of the tricky low-level faults, and so the remaining faults are usually easier to
reason about and deal with. We will explore this matter further in [“The end-to-end argument”](ch12.html#sec_future_e2e_argument). # Unreliable Networks 
As discussed in the introduction to [Part II](part02.html#part_distributed_data), the distributed systems we focus on
in this book are shared-nothing systems: i.e., a bunch of machines connected by a network. The
network is the only way those machines can communicate—we assume that each machine has its
own memory and disk, and one machine cannot access another machine’s memory or disk (except by
making requests to a service over the network).