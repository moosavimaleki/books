It is also possible to process streams using actor frameworks. However, many such frameworks do not
guarantee message delivery in the case of crashes, so the processing is not fault-tolerant unless
you implement additional retry logic. ## Reasoning About Time 
Stream processors often need to deal with time, especially when used for analytics purposes, which
frequently use time windows such as “the average over the last five minutes.” It might seem that the
meaning of “the last five minutes” should be unambiguous and clear, but unfortunately the notion is
surprisingly tricky. In a batch process, the processing tasks rapidly crunch through a large collection of historical
events. If some kind of breakdown by time needs to happen, the batch process needs to look at the
timestamp embedded in each event. There is no point in looking at the system clock of the machine
running the batch process, because the time at which the process is run has nothing to do with the
time at which the events actually occurred.