The web, and increasing numbers of HTTP/REST-based APIs, has made the request/response style of
interaction so common that it’s easy to take it for granted. But we should remember that it’s not
the only way of building systems, and that other approaches have their merits too. Let’s distinguish
three different types of systems: Services (online systems) 
A service waits for a request or instruction from a client to arrive. When one is received, the
service tries to handle it as quickly as possible and sends a response back. Response time is
usually the primary measure of performance of a service, and availability is often very important
(if the client can’t reach the service, the user will probably get an error message). Batch processing systems (offline systems) 
A batch processing system takes a large amount of input data, runs a job to process it, and
produces some output data. Jobs often take a while (from a few minutes to several days), so there
normally isn’t a user waiting for the job to finish. Instead, batch jobs are often scheduled to
run periodically (for example, once a day). The primary performance measure of a batch job is
usually throughput (the time it takes to crunch through an input dataset of a certain size). We
discuss batch processing in this chapter.