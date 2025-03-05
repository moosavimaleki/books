Tumbling window 
A tumbling window has a fixed length, and every event belongs to exactly one window. For example,
if you have a 1-minute tumbling window, all the events with timestamps between 10:03:00 and
10:03:59 are grouped into one window, events between 10:04:00 and 10:04:59 into the next window,
and so on. You could implement a 1-minute tumbling window by taking each event timestamp and
rounding it down to the nearest minute to determine the window that it belongs to. Hopping window 
A hopping window also has a fixed length, but allows windows to overlap in order to provide some
smoothing. For example, a 5-minute window with a hop size of 1 minute would contain the events
between 10:03:00 and 10:07:59, then the next window would cover events between 10:04:00 and
10:08:59, and so on. You can implement this hopping window by first calculating 1-minute tumbling
windows, and then aggregating over several adjacent windows.