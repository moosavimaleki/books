![ddia 0902](assets/ddia_0902.png) ###### Figure 9-2. If a read request is concurrent with a write request, it may return either the old or the new value. For simplicity, [Figure 9-2](#fig_consistency_linearizability_1) shows only the requests from the clients’
point of view, not the internals of the database. Each bar is a request made by a client, where the
start of a bar is the time when the request was sent, and the end of a bar is when the response was
received by the client. Due to variable network delays, a client doesn’t know exactly when the
database processed its request—it only knows that it must have happened sometime between the
client sending the request and receiving the response.[i](ch09.html#idm140605760066128) In this example, the register has two types of operations: *  read(x) ⇒ v means the client requested to read the value of register
x, and the database returned the value v. * 