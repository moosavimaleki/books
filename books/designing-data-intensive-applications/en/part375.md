### Capturing the happens-before relationship 
Let’s look at an algorithm that determines whether two operations are concurrent, or whether one
happened before another. To keep things simple, let’s start with a database that has only one
replica. Once we have worked out how to do this on a single replica, we can generalize the approach
to a leaderless database with multiple replicas. [Figure 5-13](#fig_replication_causality_single) shows two clients concurrently adding items to the same
shopping cart. (If that example strikes you as too inane, imagine instead two air traffic
controllers concurrently adding aircraft to the sector they are tracking.) Initially, the cart is
empty. Between them, the clients make five writes to the database: 1.  Client 1 adds milk to the cart. This is the first write to that key, so the server successfully
stores it and assigns it version 1. The server also echoes the value back to the client, along
with the version number.