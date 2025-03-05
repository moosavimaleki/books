
Using the MapReduce programming model has separated the physical network communication aspects of
the computation (getting the data to the right machine) from the application logic (processing the
data once you have it). This separation contrasts with the typical use of databases, where a request to
fetch data from a database often occurs somewhere deep inside a piece of application code
[[36](ch10.html#Kleppmann2012ts)].
Since MapReduce handles all network communication, it also shields the application code from having
to worry about partial failures, such as the crash of another node: MapReduce transparently retries
failed tasks without affecting the application logic. ### GROUP BY 
Besides joins, another common use of the “bringing related data to the same place” pattern is
grouping records by some key (as in the GROUP BY clause in SQL). All records with the same key
form a group, and the next step is often to perform some kind of aggregation within each group—for
example: