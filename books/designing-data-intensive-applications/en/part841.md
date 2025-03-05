When loading data into Voldemort, the server continues serving requests to the old data files while
the new data files are copied from the distributed filesystem to the server’s local disk. Once the
copying is complete, the server atomically switches over to querying the new files. If anything goes
wrong in this process, it can easily switch back to the old files again, since they are still there
and immutable [[46](ch10.html#Sumbaly2012wi)]. ### Philosophy of batch process outputs 
The Unix philosophy that we discussed earlier in this chapter ([“The Unix Philosophy”](#sec_batch_unix_philosophy))
encourages experimentation by being very explicit about dataflow: a program reads its input and
writes its output. In the process, the input is left unchanged, any previous output is completely
replaced with the new output, and there are no other side effects. This means that you can rerun a
command as often as you like, tweaking or debugging it, without messing up the state of your system.