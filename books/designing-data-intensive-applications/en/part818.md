### Example: analysis of user activity events 
A typical example of a join in a batch job is illustrated in [Figure 10-2](#fig_batch_join_example). On the left
is a log of events describing the things that logged-in users did on a website (known as activity
events or clickstream data), and on the right is a database of users. You can think of this
example as being part of a star schema (see [“Stars and Snowflakes: Schemas for Analytics”](ch03.html#sec_storage_analytics_schemas)): the log of events is
the fact table, and the user database is one of the dimensions. ![ddia 1002](assets/ddia_1002.png) ###### Figure 10-2. A join between a log of user activity events and a database of user profiles. An analytics task may need to correlate user activity with user profile information: for example, if
the profile contains the user’s age or date of birth, the system could determine which pages are
most popular with which age groups. However, the activity events contain only the user ID, not the
full user profile information. Embedding that profile information in every single activity event
would most likely be too wasteful. Therefore, the activity events need to be joined with the user
profile database.