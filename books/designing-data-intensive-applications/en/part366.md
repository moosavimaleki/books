*  Or should we accept writes anyway, and write them to some nodes that are reachable but aren’t
among the n nodes on which the value usually lives? 
The latter is known as a sloppy quorum
[[37](ch05.html#DeCandia2007ui_ch5)]: writes and reads still require w
and r successful responses, but those may include nodes that are not among the designated n
“home” nodes for a value. By analogy, if you lock yourself out of your house, you may knock on the
neighbor’s door and ask whether you may stay on their couch temporarily. 
Once the network interruption is fixed, any writes that one node temporarily accepted on behalf of
another node are sent to the appropriate “home” nodes. This is called hinted handoff. (Once you
find the keys to your house again, your neighbor politely asks you to get off their couch and go
home.) Sloppy quorums are particularly useful for increasing write availability: as long as any w nodes
are available, the database can accept writes. However, this means that even when
w + r > n, you cannot be sure to read the latest value for a key, because the
latest value may have been temporarily written to some nodes outside of n
[[47](ch05.html#Blomstedt2012vi)].