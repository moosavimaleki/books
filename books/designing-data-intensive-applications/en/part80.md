Some developers feel that the JSON model reduces the impedance mismatch between the application code
and the storage layer. However, as we shall see in [Chapter 4](ch04.html#ch_encoding), there are also problems with
JSON as a data encoding format. The lack of a schema is often cited as an advantage; we will discuss
this in [“Schema flexibility in the document model”](#sec_datamodels_schema_flexibility). 
The JSON representation has better locality than the multi-table schema in
[Figure 2-1](#fig_billgates_relational). If you want to fetch a profile in the relational example, you need to
either perform multiple queries (query each table by user_id) or perform a messy multi-way join
between the users table and its subordinate tables. In the JSON representation, all the relevant
information is in one place, and one query is sufficient. 
The one-to-many relationships from the user profile to the user’s positions, educational history, and
contact information imply a tree structure in the data, and the JSON representation makes this tree
structure explicit (see [Figure 2-2](#fig_json_tree)).