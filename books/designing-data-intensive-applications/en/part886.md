[iii](ch10.html#idm140605758280016-marker) Except by
using a separate tool, such as netcat or curl. Unix started out trying to
represent everything as files, but the BSD sockets API deviated from that convention
[[17](ch10.html#DJBTwoFD)]. The research operating systems Plan
9 and Inferno are more consistent in their use of files: they represent a TCP
connection as a file in /net/tcp
[[18](ch10.html#Pike1999ui)]. [iv](ch10.html#idm140605758239072-marker) One difference is that
with HDFS, computing tasks can be scheduled to run on the machine that stores a copy of a particular
file, whereas object stores usually keep storage and computation separate. Reading from a local disk
has a performance advantage if network bandwidth is a bottleneck. Note however that if erasure coding is
used, the locality advantage is lost, because the data from several machines must be combined in
order to reconstitute the original file
[[20](ch10.html#Ovsiannikov2013da)]. [v](ch10.html#idm140605758092544-marker) The joins we talk about
in this book are generally equi-joins, the most common type of join, in which a record is
associated with other records that have an identical value in a particular field (such as
an ID). Some databases support more general types of joins, for example using a less-than operator
instead of an equality operator, but we do not have space to cover them here.