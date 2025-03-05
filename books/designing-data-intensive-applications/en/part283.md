
Three popular distributed actor frameworks handle message encoding as follows: *  Akka uses Java’s built-in serialization by default, which does not provide forward or backward
compatibility. However, you can replace it with something like Protocol Buffers, and thus gain the
ability to do rolling upgrades [[50](ch04.html#Boner2013tx)]. *  Orleans by default uses a custom data encoding format that does not support rolling upgrade
deployments; to deploy a new version of your application, you need to set up a new cluster, move
traffic from the old cluster to the new one, and shut down the old one
[[51](ch04.html#Bernstein2014tr),
[52](ch04.html#Orleans2015)].
Like with Akka, custom serialization plug-ins can be used. *  
  In Erlang OTP it is surprisingly hard to make changes to record schemas (despite the system
  having many features designed for high availability); rolling upgrades are possible but need to be
  planned carefully
  [[53](ch04.html#Mercer2007va)].
  An experimental new maps datatype (a JSON-like structure, introduced in Erlang R17 in 2014) may
  make this easier in the future [[54](ch04.html#Hebert2014uu)].