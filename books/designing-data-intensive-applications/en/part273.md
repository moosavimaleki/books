*  If you retry a failed network request, it could happen that the requests are actually getting
through, and only the responses are getting lost.
In that case, retrying will cause the action to
be performed multiple times, unless you build a mechanism for deduplication (idempotence) into
the protocol. Local function calls don’t have this problem. (We discuss idempotence in more detail
in [Chapter 11](ch11.html#ch_stream).) *  Every time you call a local function, it normally takes about the same time to execute. A network
request is much slower than a function call, and its latency is also wildly variable: at good
times it may complete in less than a millisecond, but when the network is congested or the remote
service is overloaded it may take many seconds to do exactly the same thing. *  When you call a local function, you can efficiently pass it references (pointers) to objects in
local memory. When you make a network request, all those parameters need to be encoded into a
sequence of bytes that can be sent over the network. That’s okay if the parameters are primitives
like numbers or strings, but quickly becomes problematic with larger objects.