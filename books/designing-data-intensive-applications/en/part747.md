## Membership and Coordination Services 
Projects like ZooKeeper or etcd are often described as “distributed key-value stores” or
“coordination and configuration services.” The API of such a service looks pretty much like that of
a database: you can read and write the value for a given key, and iterate over keys. So if they’re
basically databases, why do they go to all the effort of implementing a consensus algorithm? What
makes them different from any other kind of database? 
To understand this, it is helpful to briefly explore how a service like ZooKeeper is used. As an
application developer, you will rarely need to use ZooKeeper directly, because it is actually not well
suited as a general-purpose database. It is more likely that you will end up relying on it indirectly via
some other project: for example, HBase, Hadoop YARN, OpenStack Nova, and Kafka all rely on ZooKeeper
running in the background. What is it that these projects get from it?