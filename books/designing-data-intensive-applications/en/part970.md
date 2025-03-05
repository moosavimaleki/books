In this context, the timestamp on the events should really be the time at which the user interaction
occurred, according to the mobile device’s local clock. However, the clock on a user-controlled
device often cannot be trusted, as it may be accidentally or deliberately set to the wrong time (see
[“Clock Synchronization and Accuracy”](ch08.html#sec_distributed_clock_accuracy)). The time at which the event was received by the server
(according to the server’s clock) is more likely to be accurate, since the server is under your
control, but less meaningful in terms of describing the user interaction. To adjust for incorrect device clocks, one approach is to log three timestamps
[[82](ch11.html#Dean2015tn)]: *  The time at which the event occurred, according to the device clock *  The time at which the event was sent to the server, according to the device clock *  The time at which the event was received by the server, according to the server clock