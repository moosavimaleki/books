# Relational Model Versus Document Model 
The best-known data model today is probably that of SQL, based on the relational model proposed by
Edgar Codd in 1970 [[1](ch02.html#Codd1970dg)]:
data is organized into relations (called tables in SQL), where each relation is an unordered collection
of tuples (rows in SQL). 
The relational model was a theoretical proposal, and many people at the time doubted whether it
could be implemented efficiently. However, by the mid-1980s, relational database management systems
(RDBMSes) and SQL had become the tools of choice for most people who needed to store and query data
with some kind of regular structure. The dominance of relational databases has lasted around
25‒30 years—an eternity in computing history. 
The roots of relational databases lie in business data processing, which was performed on
mainframe computers in the 1960s and ’70s. The use cases appear mundane from today’s perspective:
typically transaction processing (entering sales or banking transactions, airline reservations,
stock-keeping in warehouses) and batch processing (customer invoicing, payroll, reporting).