
If you have spent years working with transactions, they may seem obvious, but we shouldn’t take them
for granted. Transactions are not a law of nature; they were created with a purpose, namely to
simplify the programming model for applications accessing a database. By using transactions, the
application is free to ignore certain potential error scenarios and concurrency issues, because the
database takes care of them instead (we call these safety guarantees). Not every application needs transactions, and sometimes there are advantages to weakening
transactional guarantees or abandoning them entirely (for example, to achieve higher performance or
higher availability). Some safety properties can be achieved without transactions. How do you figure out whether you need transactions? In order to answer that question, we first need
to understand exactly what safety guarantees transactions can provide, and what costs are associated
with them. Although transactions seem straightforward at first glance, there are actually many
subtle but important details that come into play.