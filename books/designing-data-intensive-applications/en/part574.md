You can check the value of the monotonic clock at one point in time, do something, and then check
the clock again at a later time. The difference between the two values tells you how much time
elapsed between the two checks. However, the absolute value of the clock is meaningless: it might
be the number of nanoseconds since the computer was started, or something similarly arbitrary. In
particular, it makes no sense to compare monotonic clock values from two different computers,
because they don’t mean the same thing. On a server with multiple CPU sockets, there may be a separate timer per CPU, which is not
necessarily synchronized with other CPUs. Operating systems compensate for any discrepancy and try
to present a monotonic view of the clock to application threads, even as they are scheduled across
different CPUs. However, it is wise to take this guarantee of monotonicity with a pinch of salt
[[40](ch08.html#Loughran2015wi)].