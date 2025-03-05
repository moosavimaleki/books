
Making a system simpler does not necessarily mean reducing its functionality; it can also mean
removing accidental complexity. Moseley and Marks
[[32](ch01.html#MoseleyHo10rPt5)] define complexity as accidental if
it is not inherent in the problem that the software solves (as seen by the users) but arises only
from the implementation. 
One of the best tools we have for removing accidental complexity is abstraction. A good
abstraction can hide a great deal of implementation detail behind a clean, simple-to-understand
façade. A good abstraction can also be used for a wide range of different applications. Not only is
this reuse more efficient than reimplementing a similar thing multiple times, but it also leads to
higher-quality software, as quality improvements in the abstracted component benefit all
applications that use it. 
For example, high-level programming languages are abstractions that hide machine code, CPU registers,
and syscalls. SQL is an abstraction that hides complex on-disk and in-memory data structures,
concurrent requests from other clients, and inconsistencies after crashes. Of course, when
programming in a high-level language, we are still using machine code; we are just not using it
directly, because the programming language abstraction saves us from having to think about it.