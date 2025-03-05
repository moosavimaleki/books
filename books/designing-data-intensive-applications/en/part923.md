The only side effect of processing, besides any output of the consumer, is that the consumer offset
moves forward. But the offset is under the consumer’s control, so it can easily be manipulated if
necessary: for example, you can start a copy of a consumer with yesterday’s offsets and write the
output to a different location, in order to reprocess the last day’s worth of messages. You can
repeat this any number of times, varying the processing code. 
This aspect makes log-based messaging more like the batch processes of the last chapter, where
derived data is clearly separated from input data through a repeatable transformation process. It
allows more experimentation and easier recovery from errors and bugs, making it a good tool for
integrating dataflows within an organization [[24](ch11.html#Kreps2013vs_ch11)]. # Databases and Streams 
We have drawn some comparisons between message brokers and databases. Even though they have
traditionally been considered separate categories of tools, we saw that log-based message
brokers have been successful in taking ideas from databases and applying them to messaging. We can
also go in reverse: take ideas from messaging and streams, and apply them to databases.