*  
In [“Consistent Prefix Reads”](ch05.html#sec_replication_consistent_prefix) ([Figure 5-5](ch05.html#fig_replication_consistent_prefix)) we saw an example
where the observer of a conversation saw first the answer to a question, and then the question
being answered. This is confusing because it violates our intuition of cause and effect: if a
question is answered, then clearly the question had to be there first, because the person giving
the answer must have seen the question (assuming they are not psychic and cannot see into the
future). We say that there is a causal dependency between the question and the answer. *  A similar pattern appeared in [Figure 5-9](ch05.html#fig_replication_causality), where we looked at the replication
between three leaders and noticed that some writes could “overtake” others due to network delays.
From the perspective of one of the replicas it would look as though there was an update to a row
that did not exist. Causality here means that a row must first be created before it can be
updated.