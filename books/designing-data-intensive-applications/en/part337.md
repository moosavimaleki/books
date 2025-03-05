### Clients with offline operation 
Another situation in which multi-leader replication is appropriate is if you have an application
that needs to continue to work while it is disconnected from the internet. For example, consider the calendar apps on your mobile phone, your laptop, and other devices. You
need to be able to see your meetings (make read requests) and enter new meetings (make write
requests) at any time, regardless of whether your device currently has an internet connection. If
you make any changes while you are offline, they need to be synced with a server and your other
devices when the device is next online. 
In this case, every device has a local database that acts as a leader (it accepts write requests),
and there is an asynchronous multi-leader replication process (sync) between the replicas of your
calendar on all of your devices. The replication lag may be hours or even days, depending on when
you have internet access available.