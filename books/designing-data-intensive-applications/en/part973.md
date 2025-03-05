Sliding window 
A sliding window contains all the events that occur within some interval of each other. For
example, a 5-minute sliding window would cover events at 10:03:39 and 10:08:12, because they are
less than 5 minutes apart (note that tumbling and hopping 5-minute windows would not have put
these two events in the same window, as they use fixed boundaries). A sliding window can be
implemented by keeping a buffer of events sorted by time and removing old events when they expire
from the window. Session window 
Unlike the other window types, a session window has no fixed duration. Instead, it is defined by
grouping together all events for the same user that occur closely together in time, and the window
ends when the user has been inactive for some time (for example, if there have been no events for
30 minutes). Sessionization is a common requirement for website analytics (see
[“GROUP BY”](ch10.html#sec_batch_grouping)).