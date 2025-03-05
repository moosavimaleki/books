### Single-object writes 
Atomicity and isolation also apply when a single object is being changed. For example, imagine you
are writing a 20 KB JSON document to a database: *  If the network connection is interrupted after the first 10 KB have been sent, does the
database store that unparseable 10 KB fragment of JSON? *  If the power fails while the database is in the middle of overwriting the previous value on disk,
do you end up with the old and new values spliced together? *  If another client reads that document while the write is in progress, will it see a partially
updated value? Those issues would be incredibly confusing, so storage engines almost universally aim to provide
atomicity and isolation on the level of a single object (such as a key-value pair) on one node.
Atomicity can be implemented using a log for crash recovery (see [“Making B-trees reliable”](ch03.html#sec_storage_btree_wal)), and
isolation can be implemented using a lock on each object (allowing only one thread to access an
object at any one time).