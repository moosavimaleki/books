*  A Unix process can be paused by sending it the SIGSTOP signal, for example by pressing Ctrl-Z in
a shell. This signal immediately stops the process from getting any more CPU cycles until it is
resumed with SIGCONT, at which point it continues running where it left off. Even if your
environment does not normally use SIGSTOP, it might be sent accidentally by an operations
engineer. 
All of these occurrences can preempt the running thread at any point and resume it at some later time,
without the thread even noticing. The problem is similar to making multi-threaded code on a single
machine thread-safe: you can’t assume anything about timing, because arbitrary context switches and
parallelism may occur. When writing multi-threaded code on a single machine, we have fairly good tools for making it
thread-safe: mutexes, semaphores, atomic counters, lock-free data structures, blocking queues, and
so on. Unfortunately, these tools don’t directly translate to distributed systems, because a
distributed system has no shared memory—only messages sent over an unreliable network.