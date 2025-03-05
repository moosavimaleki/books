### Cross-channel timing dependencies 
Notice a detail in [Figure 9-1](#fig_consistency_linearizability_0): if Alice hadn’t exclaimed the score, Bob
wouldn’t have known that the result of his query was stale. He would have just refreshed the page
again a few seconds later, and eventually seen the final score. The linearizability violation was
only noticed because there was an additional communication channel in the system (Alice’s voice to
Bob’s ears). 
Similar situations can arise in computer systems. For example, say you have a website where users
can upload a photo, and a background process resizes the photos to lower resolution for faster
download (thumbnails). The architecture and dataflow of this system is illustrated in
[Figure 9-5](#fig_consistency_thumbnailer). The image resizer needs to be explicitly instructed to perform a resizing job, and this instruction
is sent from the web server to the resizer via a message queue (see [Chapter 11](ch11.html#ch_stream)). The web server
doesn’t place the entire photo on the queue, since most message brokers are designed for small
messages, and a photo may be several megabytes in size. Instead, the photo is first written to a
file storage service, and once the write is complete, the instruction to the resizer is placed on
the queue.