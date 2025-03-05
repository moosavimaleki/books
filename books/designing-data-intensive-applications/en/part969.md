2.  Publish a correction, an updated value for the window with stragglers included. You may also
need to retract the previous output. In some cases it is possible to use a special message to indicate, “From now on there will be no more
messages with a timestamp earlier than t,” which can be used by consumers to trigger windows
[[81](ch11.html#Akidau2013uz)]. However, if several producers on different machines are generating events,
each with their own minimum timestamp thresholds, the consumers need to keep track of each producer
individually. Adding and removing producers is trickier in this case. ### Whose clock are you using, anyway? 
Assigning timestamps to events is even more difficult when events can be buffered at several points
in the system. For example, consider a mobile app that reports events for usage metrics to a server.
The app may be used while the device is offline, in which case it will buffer events locally on the
device and send them to a server when an internet connection is next available (which may be hours
or even days later). To any consumers of this stream, the events will appear as extremely delayed
stragglers.