
Thus, applications that use event sourcing need to take the log of events (representing the data
written to the system) and transform it into application state that is suitable for showing to
a user (the way in which data is read from the system
[[47](ch11.html#Kleppmann2016ug)]).
This transformation can use arbitrary logic, but it should be deterministic so that you can run it
again and derive the same application state from the event log. Like with change data capture, replaying the event log allows you to reconstruct the current state
of the system. However, log compaction needs to be handled differently: *  A CDC event for the update of a record typically contains the entire new version of the record, so
the current value for a primary key is entirely determined by the most recent event for that
primary key, and log compaction can discard previous events for the same key.