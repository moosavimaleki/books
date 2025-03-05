*  If a node process crashed (or was killed by an administrator) but the node’s operating system is
still running, a script can notify other nodes about the crash so that another node can take over
quickly without having to wait for a timeout to expire. For example, HBase does this
[[23](ch08.html#Liochon2015ux)]. *  If you have access to the management interface of the network switches in your datacenter, you can
query them to detect link failures at a hardware level (e.g., if the remote machine is powered
down). This option is ruled out if you’re connecting via the internet, or if you’re in a shared
datacenter with no access to the switches themselves, or if you can’t reach the management
interface due to a network problem. *  If a router is sure that the IP address you’re trying to connect to is unreachable, it may reply
to you with an ICMP Destination Unreachable packet. However, the router doesn’t have a magic
failure detection capability either—it is subject to the same limitations as other participants
of the network.