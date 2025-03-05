*  Incrementing a counter or updating an account balance (requires reading the current value,
calculating the new value, and writing back the updated value) *  Making a local change to a complex value, e.g., adding an element to a list within a JSON document
(requires parsing the document, making the change, and writing back the modified document) *  Two users editing a wiki page at the same time, where each user saves their changes by sending the
entire page contents to the server, overwriting whatever is currently in the database Because this is such a common problem, a variety of solutions have been developed. ### Atomic write operations 
Many databases provide atomic update operations, which remove the need to implement
read-modify-write cycles in application code. They are usually the best solution if your code can be
expressed in terms of those operations. For example, the following instruction is concurrency-safe
in most relational databases: