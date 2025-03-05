# Faults and Partial Failures 
When you are writing a program on a single computer, it normally behaves in a fairly predictable
way: either it works or it doesn’t. Buggy software may give the appearance that the computer is
sometimes “having a bad day” (a problem that is often fixed by a reboot), but that is mostly just
a consequence of badly written software. 
There is no fundamental reason why software on a single computer should be flaky: when the hardware
is working correctly, the same operation always produces the same result (it is deterministic). If
there is a hardware problem (e.g., memory corruption or a loose connector), the consequence is usually a
total system failure (e.g., kernel panic, “blue screen of death,” failure to start up). An individual
computer with good software is usually either fully functional or entirely broken, but not something
in between. This is a deliberate choice in the design of computers: if an internal fault occurs, we prefer a
computer to crash completely rather than returning a wrong result, because wrong results are difficult
and confusing to deal with. Thus, computers hide the fuzzy physical reality on which they are
implemented and present an idealized system model that operates with mathematical perfection. A CPU
instruction always does the same thing; if you write some data to memory or disk, that data remains
intact and doesn’t get randomly corrupted. This design goal of always-correct computation goes all
the way back to the very first digital computer
[[3](ch08.html#Padua2015um)].