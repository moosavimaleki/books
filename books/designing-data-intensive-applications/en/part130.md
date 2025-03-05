The URL  doesn’t necessarily need to resolve to anything—from
RDF’s point of view, it is simply a namespace. To avoid potential confusion with http:// URLs, the
examples in this section use non-resolvable URIs such as urn:example:within. Fortunately, you can
just specify this prefix once at the top of the file, and then forget about it. ### The SPARQL query language SPARQL is a query language for triple-stores using the RDF data model
[[43](ch02.html#Harris2013wd)].
(It is an acronym for SPARQL Protocol and RDF Query Language, pronounced “sparkle.”)
It predates Cypher, and since Cypher’s pattern matching is borrowed from SPARQL, they look quite
similar [[37](ch02.html#Neo4j2013)]. The same query as before—finding people who have moved from the US to Europe—is even more concise
in SPARQL than it is in Cypher (see [Example 2-9](#fig_sparql_query)). ##### Example 2-9. The same query as [Example 2-4](#fig_cypher_query), expressed in SPARQL ```
`PREFIX` `:` `<``urn``:``example``:``>`

`SELECT` `?``personName` `WHERE` `{`
  `?``person` `:name` `?``personName``.`
  `?``person` `:bornIn`  `/` `:within``*` `/` `:name` `"United States"``.`
  `?``person` `:livesIn` `/` `:within``*` `/` `:name` `"Europe"``.`
`}`
```