Confusing event time and processing time leads to bad data. For example, say you have a stream
processor that measures the rate of requests (counting the number of requests per second). If you
redeploy the stream processor, it may be shut down for a minute and process the backlog of events
when it comes back up. If you measure the rate based on the processing time, it will look as if
there was a sudden anomalous spike of requests while processing the backlog, when in fact the real
rate of requests was steady ([Figure 11-7](#fig_stream_processing_time)). ![ddia 1107](assets/ddia_1107.png) ###### Figure 11-7. Windowing by processing time introduces artifacts due to variations in processing rate. ### Knowing when you’re ready 
A tricky problem when defining windows in terms of event time is that you can never be sure when you
have received all of the events for a particular window, or whether there are some events still to
come.