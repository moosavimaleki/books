*  A local function call is predictable and either succeeds or fails, depending only on parameters
that are under your control. A network request is unpredictable: the request or response may be
lost due to a network problem, or the remote machine may be slow or unavailable, and such problems
are entirely outside of your control. Network problems are common, so you have to anticipate them,
for example by retrying a failed request. *  A local function call either returns a result, or throws an exception, or never returns (because
it goes into an infinite loop or the process crashes). A network request has another possible
outcome: it may return without a result, due to a timeout. In that case, you simply don’t know
what happened: if you don’t get a response from the remote service, you have no way of knowing
whether the request got through or not. (We discuss this issue in more detail in [Chapter 8](ch08.html#ch_distributed).)