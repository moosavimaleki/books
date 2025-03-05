What remains is to discuss what you can do with the stream once you have it—namely, you can
process it. Broadly, there are three options: 1.  You can take the data in the events and write it to a database, cache, search index, or similar
storage system, from where it can then be queried by other clients. As shown in
[Figure 11-5](#fig_stream_change_capture), this is a good way of keeping a database in sync with changes
happening in other parts of the system—especially if the stream consumer is the only client
writing to the database. Writing to a storage system is the streaming equivalent of what we
discussed in [“The Output of Batch Workflows”](ch10.html#sec_batch_output). 2.  You can push the events to users in some way, for example by sending email alerts or push
notifications, or by streaming the events to a real-time dashboard where they are visualized.
In this case, a human is the ultimate consumer of the stream.