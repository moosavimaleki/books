### A system of promises 
From this short description it might not be clear why two-phase commit ensures atomicity, while
one-phase commit across several nodes does not. Surely the prepare and commit requests can just
as easily be lost in the two-phase case. What makes 2PC different? To understand why it works, we have to break down the process in a bit more detail: 1.  When the application wants to begin a distributed transaction, it requests a transaction ID from
the coordinator. This transaction ID is globally unique. 2.  The application begins a single-node transaction on each of the participants, and attaches the
globally unique transaction ID to the single-node transaction. All reads and writes are done in
one of these single-node transactions. If anything goes wrong at this stage (for example, a node
crashes or a request times out), the coordinator or any of the participants can abort. 3. 