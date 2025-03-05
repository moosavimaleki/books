*  If the client process fails while retrying, any data it was trying to write to the database is lost. # Weak Isolation Levels 
If two transactions don’t touch the same data, they can safely be run in parallel, because neither
depends on the other. Concurrency issues (race conditions) only come into play when one transaction
reads data that is concurrently modified by another transaction, or when two transactions try to
simultaneously modify the same data. Concurrency bugs are hard to find by testing, because such bugs are only triggered when you get
unlucky with the timing. Such timing issues might occur very rarely, and are usually difficult to
reproduce. Concurrency is also very difficult to reason about, especially in a large application
where you don’t necessarily know which other pieces of code are accessing the database. Application
development is difficult enough if you just have one user at a time; having many concurrent users
makes it much harder still, because any piece of data could unexpectedly change at any time.