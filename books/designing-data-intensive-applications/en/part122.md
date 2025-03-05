The answer is yes, but with some difficulty. In a relational database, you usually know in advance
which joins you need in your query. In a graph query, you may need to traverse a variable number of
edges before you find the vertex you’re looking for—that is, the number of joins is not fixed in
advance. In our example, that happens in the () -[:WITHIN*0..]-> () rule in the Cypher query. A person’s
LIVES_IN edge may point at any kind of location: a street, a city, a district, a region, a state,
etc. A city may be WITHIN a region, a region WITHIN a state, a state WITHIN a country, etc.
The LIVES_IN edge may point directly at the location vertex you’re looking for, or it may be
several levels removed in the location hierarchy. In Cypher, :WITHIN*0.. expresses that fact very concisely: it means “follow a WITHIN edge, zero
or more times.” It is like the * operator in a regular expression.