The steps may occur in a different order. For example, you could first make the write, then the
SELECT query, and finally decide whether to abort or commit based on the result of the query. In the case of the doctor on call example, the row being modified in step 3 was one of the rows
returned in step 1, so we could make the transaction safe and avoid write skew by locking the rows
in step 1 (SELECT FOR UPDATE). However, the other four examples are different: they check for the
absence of rows matching some search condition, and the write adds a row matching the same
condition. If the query in step 1 doesn’t return any rows, SELECT FOR UPDATE can’t attach locks to
anything. This effect, where a write in one transaction changes the result of a search query in another
transaction, is called a phantom [[3](ch07.html#Eswaran1976uu)].
Snapshot isolation avoids phantoms in read-only queries, but in read-write transactions like the
examples we discussed, phantoms can lead to particularly tricky cases of write skew.