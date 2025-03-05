The concatenated index approach enables an elegant data model for one-to-many relationships. For
example, on a social media site, one user may post many updates. If the primary key for updates is
chosen to be (user_id, update_timestamp), then you can efficiently retrieve all updates made by a
particular user within some time interval, sorted by timestamp. Different users may be stored on
different partitions, but within each user, the updates are stored ordered by timestamp on a single
partition. ## Skewed Workloads and Relieving Hot Spots 
As discussed, hashing a key to determine its partition can help reduce hot spots. However, it can’t
avoid them entirely: in the extreme case where all reads and writes are for the same key, you still
end up with all requests being routed to the same partition. 
This kind of workload is perhaps unusual, but not unheard of: for example, on a social media site, a
celebrity user with millions of followers may cause a storm of activity when they do something
[[14](ch06.html#Axon2010te)].
This event can result in a large volume of writes to the same key (where the key is perhaps the user ID of
the celebrity, or the ID of the action that people are commenting on). Hashing the key doesn’t
help, as the hash of two identical IDs is still the same.