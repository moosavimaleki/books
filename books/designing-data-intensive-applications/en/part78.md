
For example, [Figure 2-1](#fig_billgates_relational) illustrates how a résumé (a LinkedIn profile) could be
expressed in a relational schema. The profile as a whole can be identified by a unique identifier,
user_id. Fields like first_name and last_name appear exactly once per user, so they can be
modeled as columns on the users table. However, most people have had more than one job in their
career (positions), and people may have varying numbers of periods of education and any number of
pieces of contact information. There is a one-to-many relationship from the user to these items,
which can be represented in various ways: *  In the traditional SQL model (prior to SQL:1999), the most common normalized representation is to
put positions, education, and contact information in separate tables, with a foreign key reference
to the users table, as in [Figure 2-1](#fig_billgates_relational). *  
Later versions of the SQL standard added support for structured datatypes and XML data;
this allowed multi-valued data to be stored within a single row, with support for querying and
indexing inside those documents. These features are supported to varying degrees by Oracle, IBM
DB2, MS SQL Server, and PostgreSQL [[6](ch02.html#Wagner2010wc),
[7](ch02.html#SQLServer2013)].
A JSON datatype is also supported by several databases, including IBM DB2, MySQL, and PostgreSQL
[[8](ch02.html#PostgreSQL2013)].