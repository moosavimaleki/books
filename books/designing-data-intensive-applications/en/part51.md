
When generating load artificially in order to test the scalability of a system, the load-generating
client needs to keep sending requests independently of the response time. If the client waits for
the previous request to complete before sending the next one, that behavior has the effect of
artificially keeping the queues shorter in the test than they would be in reality, which skews the
measurements [[23](ch01.html#Treat2015vd)]. ##### Percentiles in Practice 
High percentiles become especially important in backend services that are called multiple times as
part of serving a single end-user request. Even if you make the calls in parallel, the end-user
request still needs to wait for the slowest of the parallel calls to complete. It takes just one
slow call to make the entire end-user request slow, as illustrated in [Figure 1-5](#fig_tail_amplification).
Even if only a small percentage of backend calls are slow, the chance of getting a slow call
increases if an end-user request requires multiple backend calls, and so a higher proportion of
end-user requests end up being slow (an effect known as tail latency amplification
[[24](ch01.html#tail-at-scale)]).