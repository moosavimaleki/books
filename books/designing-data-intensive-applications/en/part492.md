### Phantoms causing write skew 
All of these examples follow a similar pattern: 1.  A SELECT query checks whether some requirement is satisfied by searching for rows that
match some search condition (there are at least two doctors on call, there are no existing
bookings for that room at that time, the position on the board doesn’t already have another
figure on it, the username isn’t already taken, there is still money in the account). 2.  Depending on the result of the first query, the application code decides how to continue (perhaps
to go ahead with the operation, or perhaps to report an error to the user and abort). 3.  If the application decides to go ahead, it makes a write (INSERT, UPDATE, or DELETE) to the
database and commits the transaction. The effect of this write changes the precondition of the decision of step 2. In other words, if you
were to repeat the SELECT query from step 1 after commiting the write, you would get a different
result, because the write changed the set of rows matching the search condition (there is now one
fewer doctor on call, the meeting room is now booked for that time, the position on the board is now
taken by the figure that was moved, the username is now taken, there is now less money in the
account).