
Event sourcing is similar to the chronicle data model
[[45](ch11.html#Jagadish1995ee)], and there
are also similarities between an event log and the fact table that you find in a star schema (see
[“Stars and Snowflakes: Schemas for Analytics”](ch03.html#sec_storage_analytics_schemas)). 
Specialized databases such as Event Store
[[46](ch11.html#EventStore2016)]
have been developed to support applications using event sourcing, but in general the approach is
independent of any particular tool. A conventional database or a log-based message broker can also
be used to build applications in this style. ### Deriving current state from the event log 
An event log by itself is not very useful, because users generally expect to see the current state
of a system, not the history of modifications. For example, on a shopping website, users expect to
be able to see the current contents of their cart, not an append-only list of all the changes they
have ever made to their cart.