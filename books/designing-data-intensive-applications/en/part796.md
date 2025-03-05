## The Unix Philosophy 
It’s no coincidence that we were able to analyze a log file quite easily, using a chain of commands
like in the previous example: this was in fact one of the key design ideas of Unix, and it remains
astonishingly relevant today. Let’s look at it in some more depth so that we can borrow some ideas from
Unix [[10](ch10.html#Kleppmann2015tz_ch10)]. 
Doug McIlroy, the inventor of Unix pipes, first described them like this in 1964
[[11](ch10.html#RichieMcIlroy)]: “We should have
some ways of connecting programs like [a] garden hose—screw in another segment when it becomes
necessary to massage data in another way. This is the way of I/O also.”
The plumbing analogy stuck, and the idea of connecting programs with pipes became part of what is
now known as the Unix philosophy—a set of design principles that became popular among the
developers and users of Unix. The philosophy was described in 1978 as follows
[[12](ch10.html#McIlroy1978te), [13](ch10.html#Raymond2003wn)]: