*  On the other hand, with event sourcing, events are modeled at a higher level: an event typically
expresses the intent of a user action, not the mechanics of the state update that occurred as a
result of the action. In this case, later events typically do not override prior events, and so
you need the full history of events to reconstruct the final state. Log compaction is not possible
in the same way. Applications that use event sourcing typically have some mechanism for storing snapshots of the
current state that is derived from the log of events, so they don’t need to repeatedly reprocess
the full log. However, this is only a performance optimization to speed up reads and recovery from
crashes; the intention is that the system is able to store all raw events forever and reprocess
the full event log whenever required. We discuss this assumption in
[“Limitations of immutability”](#sec_stream_immutability_limitations).