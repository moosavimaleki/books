In this case, there are some additional issues to consider: *  Approaches that require remembering the timestamp of the user’s last update become more difficult,
because the code running on one device doesn’t know what updates have happened on the other
device. This metadata will need to be centralized. *  If your replicas are distributed across different datacenters, there is no guarantee that
  connections from different devices will be routed to the same datacenter. (For example, if the user’s desktop
  computer uses the home broadband connection and their mobile device uses the cellular data network,
  the devices’ network routes may be completely different.) If your approach requires reading from the
  leader, you may first need to route requests from all of a user’s devices to the same datacenter. ## Monotonic Reads 
Our second example of an anomaly that can occur when reading from asynchronous followers is that it’s
possible for a user to see things moving backward in time.