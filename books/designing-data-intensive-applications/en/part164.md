*  In order to serve a read request, first try to find the key in the memtable, then in the most
recent on-disk segment, then in the next-older segment, etc. *  From time to time, run a merging and compaction process in the background to combine segment files
and to discard overwritten or deleted values. This scheme works very well. It only suffers from one problem: if the database crashes, the most
recent writes (which are in the memtable but not yet written out to disk) are lost. In order to
avoid that problem, we can keep a separate log on disk to which every write is immediately appended,
just like in the previous section. That log is not in sorted order, but that doesn’t matter, because
its only purpose is to restore the memtable after a crash. Every time the memtable is written out to
an SSTable, the corresponding log can be discarded.