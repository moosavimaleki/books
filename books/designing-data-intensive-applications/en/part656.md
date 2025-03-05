![ddia 0904](assets/ddia_0904.png) ###### Figure 9-4. Visualizing the points in time at which the reads and writes appear to have taken effect. The final read by B is not linearizable. There are a few interesting details to point out in [Figure 9-4](#fig_consistency_linearizability_3): *  First client B sent a request to read x, then client D sent a request to set x to 0, and then
client A sent a request to set x to 1. Nevertheless, the value returned to B’s read is 1 (the
value written by A). This is okay: it means that the database first processed D’s write, then A’s
write, and finally B’s read. Although this is not the order in which the requests were sent, it’s
an acceptable order, because the three requests are concurrent. Perhaps B’s read request was
slightly delayed in the network, so it only reached the database after the two writes. * 