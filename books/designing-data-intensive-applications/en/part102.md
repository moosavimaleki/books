A declarative query language is attractive because it is typically more concise and easier to work
with than an imperative API. But more importantly, it also hides implementation details of the
database engine, which makes it possible for the database system to introduce performance
improvements without requiring any changes to queries. For example, in the imperative code shown at the beginning of this section, the list of animals
appears in a particular order. If the database wants to reclaim unused disk space behind the scenes,
it might need to move records around, changing the order in which the animals appear. Can the
database do that safely, without breaking queries? The SQL example doesn’t guarantee any particular ordering, and so it doesn’t mind if the order
changes. But if the query is written as imperative code, the database can never be sure whether the
code is relying on the ordering or not. The fact that SQL is more limited in functionality gives the
database much more room for automatic optimizations.