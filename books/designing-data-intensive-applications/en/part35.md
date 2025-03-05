## Software Errors 
We usually think of hardware faults as being random and independent from each other: one machine’s
disk failing does not imply that another machine’s disk is going to fail. There may be weak
correlations (for example due to a common cause, such as the temperature in the server rack), but
otherwise it is unlikely that a large number of hardware components will fail at the same time. Another class of fault is a systematic error within the system
[[8](ch01.html#Gunawi2014gn)].
Such faults are harder to anticipate, and because they are correlated across nodes, they tend to
cause many more system failures than uncorrelated hardware faults
[[5](ch01.html#Ford2010vv)]. Examples include: *  
A software bug that causes every instance of an application server to crash when given a
particular bad input. For example, consider the leap second on June 30, 2012, that caused many
applications to hang simultaneously due to a bug in the Linux kernel
[[9](ch01.html#Minar2012vh_ch1)].