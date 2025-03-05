*  When you increase a load parameter, how much do you need to increase the resources if you want to
keep performance unchanged? Both questions require performance numbers, so let’s look briefly at describing the performance of a
system. 
In a batch processing system such as Hadoop, we usually care about throughput—the number of
records we can process per second, or the total time it takes to run a job on a dataset of a certain
size.[iii](ch01.html#idm140605785971184) In online systems, what’s usually more important is the service’s
response time—that is, the time between a client sending a request and receiving a response. # Latency and response time Latency and response time are often used synonymously, but they are not the same. The response
time is what the client sees: besides the actual time to process the request (the service time),
it includes network delays and queueing delays. Latency is the duration that a request is waiting to
be handled—during which it is latent, awaiting service
[[17](ch01.html#Fowler2002wd)].