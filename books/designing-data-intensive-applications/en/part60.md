
Small software projects can have delightfully simple and expressive code, but as projects get
larger, they often become very complex and difficult to understand. This complexity slows down
everyone who needs to work on the system, further increasing the cost of maintenance. A software
project mired in complexity is sometimes described as a big ball of mud
[[30](ch01.html#Foote1997ti)]. There are various possible symptoms of complexity: explosion of the state space, tight coupling of
modules, tangled dependencies, inconsistent naming and terminology, hacks aimed at solving
performance problems, special-casing to work around issues elsewhere, and many more.
Much has been said on this topic already
[[31](ch01.html#Brooks1995wu),
[32](ch01.html#MoseleyHo10rPt5),
[33](ch01.html#Hickey2011up)]. When complexity makes maintenance hard, budgets and schedules are often overrun. In complex
software, there is also a greater risk of introducing bugs when making a change: when the system is
harder for developers to understand and reason about, hidden assumptions, unintended consequences,
and unexpected interactions are more easily overlooked. Conversely, reducing complexity greatly
improves the maintainability of software, and thus simplicity should be a key goal for the systems
we build.