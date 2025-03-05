At the point when the event is generated, it becomes a fact. Even if the customer later decides to
change or cancel the reservation, the fact remains true that they formerly held a reservation for a
particular seat, and the change or cancellation is a separate event that is added later. A consumer of the event stream is not allowed to reject an event: by the time the consumer sees the
event, it is already an immutable part of the log, and it may have already been seen by other
consumers. Thus, any validation of a command needs to happen synchronously, before it becomes an
event—for example, by using a serializable transaction that atomically validates the command and
publishes the event. Alternatively, the user request to reserve a seat could be split into two events: first a tentative
reservation, and then a separate confirmation event once the reservation has been validated (as
discussed in [“Implementing linearizable storage using total order broadcast”](ch09.html#sec_consistency_abcast_to_lin)). This split allows the validation to take place in
an asynchronous process.