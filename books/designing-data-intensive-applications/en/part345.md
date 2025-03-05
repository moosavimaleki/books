Note that conflict resolution usually applies at the level of an individual row or document, not for
an entire transaction [[36](ch05.html#Berton2016wh)].
Thus, if you have a transaction that atomically makes several different writes (see
[Chapter 7](ch07.html#ch_transactions)), each write is still considered separately for the purposes of conflict resolution. ##### Automatic Conflict Resolution 
Conflict resolution rules can quickly become complicated, and custom code can be error-prone. Amazon
is a frequently cited example of surprising effects due to a conflict resolution handler: for some
time, the conflict resolution logic on the shopping cart would preserve items added to the cart, but
not items removed from the cart. Thus, customers would sometimes see items reappearing in their
carts even though they had previously been removed
[[37](ch05.html#DeCandia2007ui_ch5)]. There has been some interesting research into automatically resolving conflicts caused by concurrent
data modifications. A few lines of research are worth mentioning: *  Conflict-free replicated datatypes (CRDTs)
[[32](ch05.html#Kleppmann2016ve),
[38](ch05.html#Shapiro2011wy)] are a family of data structures for sets, maps, ordered lists, counters,
etc. that can be concurrently edited by multiple users, and which automatically resolve conflicts
in sensible ways. Some CRDTs have been implemented in Riak 2.0
[[39](ch05.html#Elliott2013ua),
[40](ch05.html#Brown2013wy)].