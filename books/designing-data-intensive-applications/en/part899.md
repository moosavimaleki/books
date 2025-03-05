
In reality, a lot of data is unbounded because it arrives gradually over time: your users produced
data yesterday and today, and they will continue to produce more data tomorrow. Unless you go out of
business, this process never ends, and so the dataset is never “complete” in any meaningful way
[[1](ch11.html#Akidau2015gh)].
Thus, batch processors must artificially divide the data into chunks of fixed duration: for example,
processing a day’s worth of data at the end of every day, or processing an hour’s worth of data at
the end of every hour. The problem with daily batch processes is that changes in the input are only reflected in the output
a day later, which is too slow for many impatient users. To reduce the delay, we can run the
processing more frequently—say, processing a second’s worth of data at the end of every second—or
even continuously, abandoning the fixed time slices entirely and simply processing every event as it
happens. That is the idea behind stream processing.