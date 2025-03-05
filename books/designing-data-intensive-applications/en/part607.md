Let’s assume that every time the lock server grants a lock or lease, it also returns a fencing
token, which is a number that increases every time a lock is granted (e.g., incremented by the lock
service). We can then require that every time a client sends a write request to the storage service,
it must include its current fencing token. In [Figure 8-5](#fig_distributed_io_fencing_tokens), client 1 acquires the lease with a token of 33, but then
it goes into a long pause and the lease expires. Client 2 acquires the lease with a token of 34 (the
number always increases) and then sends its write request to the storage service, including the
token of 34. Later, client 1 comes back to life and sends its write to the storage service,
including its token value 33. However, the storage server remembers that it has already processed a
write with a higher token number (34), and so it rejects the request with token 33.