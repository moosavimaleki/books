Claiming a username On a website where each user has a unique username, two users may try to create accounts with the
same username at the same time. You may use a transaction to check whether a name is taken and, if
not, create an account with that name. However, like in the previous examples, that is not safe
under snapshot isolation. Fortunately, a unique constraint is a simple solution here (the second
transaction that tries to register the username will be aborted due to violating the constraint). Preventing double-spending A service that allows users to spend money or points needs to check that a user doesn’t spend more
than they have. You might implement this by inserting a tentative spending item into a user’s
account, listing all the items in the account, and checking that the sum is positive
[[44](ch07.html#Fredericks2015pg_ch7)].
With write skew, it could happen that two spending items are inserted concurrently that together
cause the balance to go negative, but that neither transaction notices the other.