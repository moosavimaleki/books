## Setting Up New Followers 
From time to time, you need to set up new followers—perhaps to increase the number of replicas,
or to replace failed nodes. How do you ensure that the new follower has an accurate copy of the
leader’s data? Simply copying data files from one node to another is typically not sufficient: clients are
constantly writing to the database, and the data is always in flux, so a standard file copy would
see different parts of the database at different points in time. The result might not make any
sense. You could make the files on disk consistent by locking the database (making it unavailable for
writes), but that would go against our goal of high availability. Fortunately, setting up a
follower can usually be done without downtime. Conceptually, the process looks like this: 1.  
Take a consistent snapshot of the leader’s database at some point in time—if possible, without
taking a lock on the entire database. Most databases have this feature, as it is also required
for backups. In some cases, third-party tools are needed, such as innobackupex for MySQL
[[12](ch05.html#Xtrabackup2014)].