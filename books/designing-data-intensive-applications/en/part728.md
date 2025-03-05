
XA is not a network protocol—it is merely a C API for interfacing with a transaction coordinator.
Bindings for this API exist in other languages; for example, in the world of Java EE applications,
XA transactions are implemented using the Java Transaction API (JTA), which in turn is supported by
many drivers for databases using Java Database Connectivity (JDBC) and drivers for message brokers
using the Java Message Service (JMS) APIs. XA assumes that your application uses a network driver or client library to communicate with the
participant databases or messaging services. If the driver supports XA, that means it calls the XA
API to find out whether an operation should be part of a distributed transaction—and if so, it
sends the necessary information to the database server. The driver also exposes callbacks through
which the coordinator can ask the participant to prepare, commit, or abort. The transaction coordinator implements the XA API. The standard does not specify how it should be
implemented, but in practice the coordinator is often simply a library that is loaded into the same
process as the application issuing the transaction (not a separate service). It keeps track of the
participants in a transaction, collects partipants’ responses after asking them to prepare (via a
callback into the driver), and uses a log on the local disk to keep track of the commit/abort
decision for each transaction.