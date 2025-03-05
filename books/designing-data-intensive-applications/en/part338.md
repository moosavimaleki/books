From an architectural point of view, this setup is essentially the same as multi-leader replication
between datacenters, taken to the extreme: each device is a “datacenter,” and the network connection
between them is extremely unreliable. As the rich history of broken calendar sync implementations
demonstrates, multi-leader replication is a tricky thing to get right. 
There are tools that aim to make this kind of multi-leader configuration easier. For example,
CouchDB is designed for this mode of operation
[[29](ch05.html#Anderson2010wj)]. ### Collaborative editing Real-time collaborative editing applications allow several people to edit a document
simultaneously. For example, Etherpad [[30](ch05.html#AppJetInc2011um)]
and Google Docs [[31](ch05.html#DayRichter2010tt)] allow multiple people to concurrently edit a text document or spreadsheet
(the algorithm is briefly discussed in [“Automatic Conflict Resolution”](#sidebar_conflict_resolution)). We don’t usually think of collaborative editing as a database replication problem, but it has a lot
in common with the previously mentioned offline editing use case. When one user edits a document,
the changes are instantly applied to their local replica (the state of the document in their web
browser or client application) and asynchronously replicated to the server and any other users who
are editing the same document.