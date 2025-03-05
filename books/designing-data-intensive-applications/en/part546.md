*  The bigger a system gets, the more likely it is that one of its components is broken. Over time,
broken things get fixed and new things break, but in a system with thousands of nodes, it is
reasonable to assume that something is always broken
[[7](ch08.html#Barroso2013ba)]. When the error handling strategy
consists of simply giving up, a large system can end up spending a lot of its time recovering from
faults rather than doing useful work [[8](ch08.html#Fiala2012ti)]. *  If the system can tolerate failed nodes and still keep working as a whole, that is a very useful
feature for operations and maintenance: for example, you can perform a rolling upgrade (see
[Chapter 4](ch04.html#ch_encoding)), restarting one node at a time, while the service continues serving users without
interruption. In cloud environments, if one virtual machine is not performing well, you can just
kill it and request a new one (hoping that the new one will be faster).