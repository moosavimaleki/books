## Solutions for Replication Lag When working with an eventually consistent system, it is worth thinking about how the application
behaves if the replication lag increases to several minutes or even hours. If the answer is “no
problem,” that’s great. However, if the result is a bad experience for users, it’s important to
design the system to provide a stronger guarantee, such as read-after-write. Pretending that
replication is synchronous when in fact it is asynchronous is a recipe for problems down the line. As discussed earlier, there are ways in which an application can provide a stronger guarantee than
the underlying database—for example, by performing certain kinds of reads on the leader. However,
dealing with these issues in application code is complex and easy to get wrong. It would be better if application developers didn’t have to worry about subtle replication issues
and could just trust their databases to “do the right thing.” This is why transactions exist: they
are a way for a database to provide stronger guarantees so that the application can be simpler.