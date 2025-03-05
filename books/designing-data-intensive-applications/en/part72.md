3.  The engineers who built your database software decided on a way of representing that
JSON/XML/relational/graph data in terms of bytes in memory, on disk, or on a network. The
representation may allow the data to be queried, searched, manipulated, and processed in various
ways. 4.  On yet lower levels, hardware engineers have figured out how to represent bytes in terms of
electrical currents, pulses of light, magnetic fields, and more. 
In a complex application there may be more intermediary levels, such as APIs built upon APIs, but
the basic idea is still the same: each layer hides the complexity of the layers below it by
providing a clean data model. These abstractions allow different groups of people—for example,
the engineers at the database vendor and the application developers using their database—to work
together effectively. There are many different kinds of data models, and every data model embodies assumptions about how
it is going to be used. Some kinds of usage are easy and some are not supported; some operations are
fast and some perform badly; some data transformations feel natural and some are awkward.