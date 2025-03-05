CEP systems often use a high-level declarative query language like SQL, or a graphical user
interface, to describe the patterns of events that should be detected. These queries are submitted to
a processing engine that consumes the input streams and internally maintains a state machine that
performs the required matching. When a match is found, the engine emits a complex event (hence the
name) with the details of the event pattern that was detected
[[67](ch11.html#Arasu2006df)]. In these systems, the relationship between queries and data is reversed compared to normal
databases. Usually, a database stores data persistently and treats queries as transient: when a
query comes in, the database searches for data matching the query, and then forgets about the query
when it has finished.  CEP engines reverse these roles: queries are stored long-term, and events
from the input streams continuously flow past them in search of a query that matches an event pattern
[[68](ch11.html#Hyde2009jm)].