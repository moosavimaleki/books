In this chapter, we will look at MapReduce and several other batch processing algorithms and
frameworks, and explore how they are used in modern data systems. But first, to get started, we will
look at data processing using standard Unix tools. Even if you are already familiar with them, a
reminder about the Unix philosophy is worthwhile because the ideas and lessons from Unix carry over
to large-scale, heterogeneous distributed data systems. # Batch Processing with Unix Tools 
Let’s start with a simple example. Say you have a web server that appends a line to a log file every
time it serves a request. For example, using the nginx default access log format, one line of the
log might look like this: ```
216.58.210.78 - - [27/Feb/2015:17:55:11 +0000] "GET /css/typography.css HTTP/1.1"
200 3377 "http://martin.kleppmann.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X
10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115
Safari/537.36"
``` (That is actually one line; it’s only broken onto multiple lines here for readability.) There’s a
lot of information in that line. In order to interpret it, you need to look at the definition of
the log format, which is as follows: