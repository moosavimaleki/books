Crash recovery If the database is restarted, the in-memory hash maps are lost. In principle, you can restore each
segment’s hash map by reading the entire segment file from beginning to end and noting the offset
of the most recent value for every key as you go along. However, that might take a long time if
the segment files are large, which would make server restarts painful.

Bitcask speeds up recovery by storing a snapshot of each segment’s hash map on disk, which can be
loaded into memory more quickly. Partially written records The database may crash at any time, including halfway through appending a record to the log.
Bitcask files include checksums, allowing such corrupted parts of the log to be detected and
ignored. Concurrency control As writes are appended to the log in a strictly sequential order, a common implementation choice
is to have only one writer thread. Data file segments are append-only and otherwise immutable, so
they can be read concurrently by multiple threads.