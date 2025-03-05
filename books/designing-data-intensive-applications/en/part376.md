2.  Client 2 adds eggs to the cart, not knowing that client 1 concurrently added milk (client 2
thought that its eggs were the only item in the cart). The server assigns version 2 to this
write, and stores eggs and milk as two separate values. It then returns both values to the
client, along with the version number of 2. 3.  Client 1, oblivious to client 2’s write, wants to add flour to the cart, so it thinks the
current cart contents should be [milk, flour]. It sends this value to the server, along with
the version number 1 that the server gave client 1 previously. The server can tell from the
version number that the write of [milk, flour] supersedes the prior value of [milk] but that
it is concurrent with [eggs]. Thus, the server assigns version 3 to [milk, flour], overwrites
the version 1 value [milk], but keeps the version 2 value [eggs] and returns both remaining
values to the client.