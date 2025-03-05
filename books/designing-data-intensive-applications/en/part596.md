# Is real-time really real? In embedded systems, real-time means that a system is carefully designed and tested to meet
specified timing guarantees in all circumstances. This meaning is in contrast to the more vague use of the
term real-time on the web, where it describes servers pushing data to clients and stream
processing without hard response time constraints (see [Chapter 11](ch11.html#ch_stream)). For example, if your car’s onboard sensors detect that you are currently experiencing a crash, you
wouldn’t want the release of the airbag to be delayed due to an inopportune GC pause in the airbag
release system. Providing real-time guarantees in a system requires support from all levels of the software stack: a
real-time operating system (RTOS) that allows processes to be scheduled with a guaranteed
allocation of CPU time in specified intervals is needed; library functions must document their
worst-case execution times; dynamic memory allocation may be restricted or disallowed entirely
(real-time garbage collectors exist, but the application must still ensure that it doesn’t give the
GC too much work to do); and an enormous amount of testing and measurement must be done to ensure
that guarantees are being met.