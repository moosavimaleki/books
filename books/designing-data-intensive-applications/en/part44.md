The final twist of the Twitter anecdote: now that approach 2 is robustly implemented, Twitter is
moving to a hybrid of both approaches. Most users’ tweets continue to be fanned out to home
timelines at the time when they are posted, but a small number of users with a very large number of
followers (i.e., celebrities) are excepted from this fan-out. Tweets from any celebrities that a
user may follow are fetched separately and merged with that user’s home timeline when it is read,
like in approach 1. This hybrid approach is able to deliver consistently good performance. We will
revisit this example in [Chapter 12](ch12.html#ch_future) after we have covered some more technical ground. ## Describing Performance 
Once you have described the load on your system, you can investigate what happens when the load
increases. You can look at it in two ways: *  When you increase a load parameter and keep the system resources (CPU, memory, network bandwidth,
etc.) unchanged, how is the performance of your system affected?