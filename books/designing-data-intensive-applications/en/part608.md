
If ZooKeeper is used as lock service, the transaction ID zxid or the node version
cversion can
be used as fencing token. Since they are guaranteed to be monotonically increasing, they have the
required properties [[74](ch08.html#Junqueira2013wi_ch8)]. Note that this mechanism requires the resource itself to take an active role in checking tokens by rejecting any
writes with an older token than one that has already been processed—it is not sufficient to rely on clients checking
their lock status themselves. For resources that do not explicitly support fencing tokens, you might
still be able work around the limitation (for example, in the case of a file storage service you
could include the fencing token in the filename). However, some kind of check is necessary to avoid
processing requests outside of the lock’s protection. Checking a token on the server side may seem like a downside, but it is arguably a good thing: it is
unwise for a service to assume that its clients will always be well behaved, because the clients are
often run by people whose priorities are very different from the priorities of the people running
the service [[76](ch08.html#McCaffrey2015ui)]. Thus, it is a good idea for any service to protect itself from accidentally
abusive clients.