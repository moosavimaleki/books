The problem is an example of what we discussed in [“Process Pauses”](#sec_distributed_clocks_pauses): if the client
holding the lease is paused for too long, its lease expires. Another client can obtain a lease for
the same file, and start writing to the file. When the paused client comes back, it believes
(incorrectly) that it still has a valid lease and proceeds to also write to the file. As a result,
the clients’ writes clash and corrupt the file. ### Fencing tokens 
When using a lock or lease to protect access to some resource, such as the file storage in
[Figure 8-4](#fig_distributed_io_fencing), we need to ensure that a node that is under a false belief of being
“the chosen one” cannot disrupt the rest of the system. A fairly simple technique that achieves this
goal is called fencing, and is illustrated in [Figure 8-5](#fig_distributed_io_fencing_tokens). ![ddia 0805](assets/ddia_0805.png) ###### Figure 8-5. Making access to storage safe by allowing writes only in the order of increasing fencing tokens.