
Even though databases started being used for many different kinds of data—comments on blog posts,
actions in a game, contacts in an address book, etc.—the basic access pattern remained similar to
processing business transactions. An application typically looks up a small number of records by
some key, using an index. Records are inserted or updated based on the user’s input.  Because these
applications are interactive, the access pattern became known as online transaction processing
(OLTP). 
However, databases also started being increasingly used for data analytics, which has very
different access patterns. Usually an analytic query needs to scan over a huge number of records,
only reading a few columns per record, and calculates aggregate statistics (such as count, sum, or
average) rather than returning the raw data to the user. For example, if your data is a table of
sales transactions, then analytic queries might be: *  What was the total revenue of each of our stores in January?