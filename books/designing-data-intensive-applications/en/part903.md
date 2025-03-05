
Databases have traditionally not supported this kind of notification mechanism very well: relational
databases commonly have triggers, which can react to a change (e.g., a row being inserted into a
table), but they are very limited in what they can do and have been somewhat of an afterthought in
database design
[[4](ch11.html#Hellerstein2005tj),
[5](ch11.html#Carney2002um)]. Instead, specialized tools have been developed for the purpose of
delivering event notifications. ## Messaging Systems A common approach for notifying consumers about new events is to use a messaging system: a
producer sends a message containing the event, which is then pushed to consumers. We touched on
these systems previously in [“Message-Passing Dataflow”](ch04.html#sec_encoding_dataflow_msg), but we will now go into more detail. A direct communication channel like a Unix pipe or TCP connection between producer and consumer
would be a simple way of implementing a messaging system. However, most messaging systems expand on
this basic model. In particular, Unix pipes and TCP connect exactly one sender with one recipient,
whereas a messaging system allows multiple producer nodes to send messages to the same topic and
allows multiple consumer nodes to receive messages in a topic.