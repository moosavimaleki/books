However, that is not the end of the list of potential race conditions that can occur between
concurrent writes. In this section we will see some subtler examples of conflicts. 
To begin, imagine this example: you are writing an application for doctors to manage their on-call
shifts at a hospital. The hospital usually tries to have several doctors on call at any one time,
but it absolutely must have at least one doctor on call. Doctors can give up their shifts (e.g., if
they are sick themselves), provided that at least one colleague remains on call in that shift
[[40](ch07.html#Cahill2008eg),
[41](ch07.html#Ports2012uw)]. 
Now imagine that Alice and Bob are the two on-call doctors for a particular shift. Both are feeling
unwell, so they both decide to request leave. Unfortunately, they happen to click the button to go
off call at approximately the same time. What happens next is illustrated in
[Figure 7-8](#fig_transactions_write_skew).