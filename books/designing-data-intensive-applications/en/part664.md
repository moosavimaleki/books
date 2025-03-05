![ddia 0905](assets/ddia_0905.png) ###### Figure 9-5. The web server and image resizer communicate both through file storage and a message queue, opening the potential for race conditions. If the file storage service is linearizable, then this system should work fine. If it is not
linearizable, there is the risk of a race condition: the message queue (steps 3 and 4 in
[Figure 9-5](#fig_consistency_thumbnailer)) might be faster than the internal replication inside the storage
service. In this case, when the resizer fetches the image (step 5), it might see an old version of
the image, or nothing at all. If it processes an old version of the image, the full-size and resized
images in the file storage become permanently inconsistent. This problem arises because there are two different communication channels between the web server
and the resizer: the file storage and the message queue. Without the recency guarantee of
linearizability, race conditions between these two channels are possible. This situation is analogous to
[Figure 9-1](#fig_consistency_linearizability_0), where there was also a race condition between two
communication channels: the database replication and the real-life audio channel between Alice’s
mouth and Bob’s ears.