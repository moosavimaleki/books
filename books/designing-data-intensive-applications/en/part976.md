
To implement this type of join, a stream processor needs to maintain state: for example, all the
events that occurred in the last hour, indexed by session ID. Whenever a search event or click event
occurs, it is added to the appropriate index, and the stream processor also checks the other index
to see if another event for the same session ID has already arrived. If there is a matching event,
you emit an event saying which search result was clicked. If the search event expires without you
seeing a matching click event, you emit an event saying which search results were not clicked. ### Stream-table join (stream enrichment) 
In [“Example: analysis of user activity events”](ch10.html#sec_batch_join_example) ([Figure 10-2](ch10.html#fig_batch_join_example)) we saw an example of a batch job joining
two datasets: a set of user activity events and a database of user profiles. It is natural to think
of the user activity events as a stream, and to perform the same join on a continuous basis in a
stream processor: the input is a stream of activity events containing a user ID, and the output is a
stream of activity events in which the user ID has been augmented with profile information about the
user. This process is sometimes known as enriching the activity events with information from the
database.