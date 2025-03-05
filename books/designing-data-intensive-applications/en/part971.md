By subtracting the second timestamp from the third, you can estimate the offset between the device
clock and the server clock (assuming the network delay is negligible compared to the required
timestamp accuracy). You can then apply that offset to the event timestamp, and thus estimate the
true time at which the event actually occurred (assuming the device clock offset did not change
between the time the event occurred and the time it was sent to the server). This problem is not unique to stream processing—batch processing suffers from exactly the same
issues of reasoning about time. It is just more noticeable in a streaming context, where we are more
aware of the passage of time. ### Types of windows 
Once you know how the timestamp of an event should be determined, the next step is to decide how
windows over time periods should be defined. The window can then be used for aggregations, for
example to count events, or to calculate the average of values within the window. Several types of
windows are in common use [[79](ch11.html#Akidau2016tb),
[83](ch11.html#AzureWindowing)]: