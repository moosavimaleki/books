An index is an additional structure that is derived from the primary data. Many databases allow
you to add and remove indexes, and this doesn’t affect the contents of the database; it only affects
the performance of queries. Maintaining additional structures incurs overhead, especially on writes. For
writes, it’s hard to beat the performance of simply appending to a file, because that’s the simplest
possible write operation. Any kind of index usually slows down writes, because the index also needs
to be updated every time data is written. This is an important trade-off in storage systems: well-chosen indexes speed up read queries, but
every index slows down writes. For this reason, databases don’t usually index everything by default,
but require you—the application developer or database administrator—to choose indexes
manually, using your knowledge of the application’s typical query patterns. You can then choose the
indexes that give your application the greatest benefit, without introducing more overhead than
necessary.