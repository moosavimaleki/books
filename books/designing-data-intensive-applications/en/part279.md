*  It can act as a buffer if the recipient is unavailable or overloaded, and thus improve system
reliability. *  It can automatically redeliver messages to a process that has crashed, and thus prevent messages from
being lost. *  It avoids the sender needing to know the IP address and port number of the recipient (which is
particularly useful in a cloud deployment where virtual machines often come and go). *  It allows one message to be sent to several recipients. *  It logically decouples the sender from the recipient (the sender just publishes messages and
doesn’t care who consumes them). However, a difference compared to RPC is that message-passing communication is usually one-way: a
sender normally doesn’t expect to receive a reply to its messages. It is possible for a process to
send a response, but this would usually be done on a separate channel. This communication pattern is
asynchronous: the sender doesn’t wait for the message to be delivered, but simply sends it and
then forgets about it.