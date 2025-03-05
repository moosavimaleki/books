
However, the downside of key range partitioning is that certain access patterns can lead to hot
spots. If the key is a timestamp, then the partitions correspond to ranges of time—e.g., one
partition per day. Unfortunately, because we write data from the sensors to the database as the
measurements happen, all the writes end up going to the same partition (the one for today), so that
partition can be overloaded with writes while others sit idle
[[5](ch06.html#Lan2011tt)]. To avoid this problem in the sensor database, you need to use something other than the timestamp as
the first element of the key. For example, you could prefix each timestamp with the sensor name so
that the partitioning is first by sensor name and then by time. Assuming you have many sensors
active at the same time, the write load will end up more evenly spread across the partitions. Now,
when you want to fetch the values of multiple sensors within a time range, you need to perform a
separate range query for each sensor name.