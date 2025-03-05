Moreover, message delays can also lead to unpredictable ordering of messages. For example, say a user
first makes one web request (which is handled by web server A), and then a second request (which is
handled by server B). A and B emit events describing the requests they handled, but B’s event
reaches the message broker before A’s event does. Now stream processors will first see the B event
and then the A event, even though they actually occurred in the opposite order. 
If it helps to have an analogy, consider the Star Wars movies: Episode IV was released in 1977,
Episode V in 1980, and Episode VI in 1983, followed by Episodes I, II, and III in 1999, 2002, and 2005,
respectively, and Episode VII in 2015 [[80](ch11.html#Ewen2016tz)].[ii](ch11.html#idm140605756499312) If you watched the movies in the order
they came out, the order in which you processed the movies is inconsistent with the order of their
narrative. (The episode number is like the event timestamp, and the date when you watched the movie
is the processing time.) As humans, we are able to cope with such discontinuities, but stream
processing algorithms need to be specifically written to accommodate such timing and ordering
issues.