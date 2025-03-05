For example, say you’re grouping events into one-minute windows so that you can count the number of
requests per minute. You have counted some number of events with timestamps that fall in the 37th
minute of the hour, and time has moved on; now most of the incoming events fall within the
38th and 39th minutes of the hour. When do you declare that you have finished the window for the 37th
minute, and output its counter value? 
You can time out and declare a window ready after you have not seen any new events for a while, but
it could still happen that some events were buffered on another machine somewhere, delayed due to a
network interruption. You need to be able to handle such straggler events that arrive after the
window has already been declared complete. Broadly, you have two options
[[1](ch11.html#Akidau2015gh)]: 1.  Ignore the straggler events, as they are probably a small percentage of events in normal
circumstances. You can track the number of dropped events as a metric, and alert if you start
dropping a significant amount of data.