*  In event sourcing, the application logic is explicitly built on the basis of immutable events that
are written to an event log. In this case, the event store is append-only, and updates or deletes
are discouraged or prohibited. Events are designed to reflect things that happened at the
application level, rather than low-level state changes. Event sourcing is a powerful technique for data modeling: from an application point of view it is
more meaningful to record the user’s actions as immutable events, rather than recording the effect
of those actions on a mutable database. Event sourcing makes it easier to evolve applications over
time, helps with debugging by making it easier to understand after the fact why something happened,
and guards against application bugs (see [“Advantages of immutable events”](#sec_stream_immutability_pros)). For example, storing the event “student cancelled their course enrollment” clearly expresses the
intent of a single action in a neutral fashion, whereas the side effects “one entry was deleted from
the enrollments table, and one cancellation reason was added to the student feedback table” embed a
lot of assumptions about the way the data is later going to be used. If a new application feature is
introduced—for example, “the place is offered to the next person on the waiting list”—the event
sourcing approach allows that new side effect to easily be chained off the existing event.