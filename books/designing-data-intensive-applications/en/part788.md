
MapReduce is a fairly low-level programming model compared to the parallel processing systems that
were developed for data warehouses many years previously
[[3](ch10.html#Babu2013gm_ch10),
[4](ch10.html#DeWitt2008up)],
but it was a major step forward in terms of the scale of processing that could be achieved on
commodity hardware. Although the importance of MapReduce is now declining
[[5](ch10.html#Robinson2014vz)],
it is still worth understanding, because it provides a clear picture of why and how batch processing
is useful. 
In fact, batch processing is a very old form of computing. Long before programmable digital
computers were invented, punch card tabulating machines—such as the Hollerith machines used in
the 1890 US Census
[[6](ch10.html#Hollerith)]—implemented a
semi-mechanized form of batch processing to compute aggregate statistics from large inputs. And
MapReduce bears an uncanny resemblance to the electromechanical IBM card-sorting machines that were
widely used for business data processing in the 1940s and 1950s
[[7](ch10.html#IBM1962vz)]. As usual, history has a tendency of repeating
itself.