![ddia 0104](assets/ddia_0104.png) ###### Figure 1-4. Illustrating mean and percentiles: response times for a sample of 100 requests to a service. 
It’s common to see the average response time of a service reported. (Strictly speaking, the term
“average” doesn’t refer to any particular formula, but in practice it is usually understood as the
arithmetic mean: given n values, add up all the values, and divide by n.) However,
the mean is not a very good metric if you want to know your “typical” response time, because it
doesn’t tell you how many users actually experienced that delay. 
Usually it is better to use percentiles. If you take your list of response times and sort it from
fastest to slowest, then the median is the halfway point: for example, if your median response
time is 200 ms, that means half your requests return in less than 200 ms, and half your
requests take longer than that.