![ddia 0708](assets/ddia_0708.png) ###### Figure 7-8. Example of write skew causing an application bug. In each transaction, your application first checks that two or more doctors are currently on call;
if yes, it assumes it’s safe for one doctor to go off call. Since the database is using snapshot
isolation, both checks return 2, so both transactions proceed to the next stage. Alice updates her
own record to take herself off call, and Bob updates his own record likewise. Both transactions
commit, and now no doctor is on call. Your requirement of having at least one doctor on call has
been violated. ### Characterizing write skew This anomaly is called write skew [[28](ch07.html#Berenson1995kj)]. It
is neither a dirty write nor a lost update, because the two transactions are updating two different
objects (Alice’s and Bob’s on-call records, respectively). It is less obvious that a conflict occurred
here, but it’s definitely a race condition: if the two transactions had run one after another, the
second doctor would have been prevented from going off call. The anomalous behavior was only
possible because the transactions ran concurrently.