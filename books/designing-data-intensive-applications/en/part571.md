1.  Has this request timed out yet? 2.  What’s the 99th percentile response time of this service? 3.  How many queries per second did this service handle on average in the last five minutes? 4.  How long did the user spend on our site? 5.  When was this article published? 6.  At what date and time should the reminder email be sent? 7.  When does this cache entry expire? 8.  What is the timestamp on this error message in the log file? 
Examples 1–4 measure durations (e.g., the time interval between a request being sent and a
response being received), whereas examples 5–8 describe points in time (events that occur on a
particular date, at a particular time). 
In a distributed system, time is a tricky business, because communication is not instantaneous: it
takes time for a message to travel across the network from one machine to another. The time when a
message is received is always later than the time when it is sent, but due to variable delays in the
network, we don’t know how much later. This fact sometimes makes it difficult to determine the order
in which things happened when multiple machines are involved.