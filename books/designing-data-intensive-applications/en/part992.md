We distinguished three types of joins that may appear in stream processes: Stream-stream joins Both input streams consist of activity events, and the join operator searches for related events
that occur within some window of time. For example, it may match two actions taken by the same
user within 30 minutes of each other.
 The two join inputs may in fact be the same stream (a self-join) if you want
to find related events within that one stream. Stream-table joins One input stream consists of activity events, while the other is a database changelog. The
changelog keeps a local copy of the database up to date. For each activity event, the join
operator queries the database and outputs an enriched activity event. Table-table joins Both input streams are database changelogs. In this case, every change on one side is joined with
the latest state of the other side. The result is a stream of changes to the materialized view of
the join between the two tables.