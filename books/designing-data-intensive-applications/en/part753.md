### Service discovery 
ZooKeeper, etcd, and Consul are also often used for service discovery—that is, to find out which
IP address you need to connect to in order to reach a particular service. In cloud datacenter
environments, where it is common for virtual machines to continually come and go, you often don’t
know the IP addresses of your services ahead of time. Instead, you can configure your services such
that when they start up they register their network endpoints in a service registry, where they can
then be found by other services. 
However, it is less clear whether service discovery actually requires consensus. DNS is the
traditional way of looking up the IP address for a service name, and it uses multiple layers of
caching to achieve good performance and availability. Reads from DNS are absolutely not
linearizable, and it is usually not considered problematic if the results from a DNS query are a
little stale [[109](ch09.html#Fournier2015wt)].
It is more important that DNS is reliably available and robust to network interruptions.