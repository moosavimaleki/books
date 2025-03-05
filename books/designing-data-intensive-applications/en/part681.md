
Read skew (non-repeatable reads, as illustrated in [Figure 7-6](ch07.html#fig_transactions_item_many_preceders)) means
reading data in a state that violates causality. *  Our examples of write skew between transactions (see [“Write Skew and Phantoms”](ch07.html#sec_transactions_write_skew)) also
demonstrated causal dependencies: in [Figure 7-8](ch07.html#fig_transactions_write_skew), Alice was allowed to go
off call because the transaction thought that Bob was still on call, and vice versa. In this case,
the action of going off call is causally dependent on the observation of who is currently on call.
Serializable snapshot isolation (see [“Serializable Snapshot Isolation (SSI)”](ch07.html#sec_transactions_ssi)) detects write skew by tracking the
causal dependencies between transactions. *  In the example of Alice and Bob watching football ([Figure 9-1](#fig_consistency_linearizability_0)), the
fact that Bob got a stale result from the server after hearing Alice exclaim the result is a
causality violation: Alice’s exclamation is causally dependent on the announcement of the score,
so Bob should also be able to see the score after hearing Alice. The same pattern appeared again
in [“Cross-channel timing dependencies”](#sec_consistency_multi_channel) in the guise of an image resizing service.