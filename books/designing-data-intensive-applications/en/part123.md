
Since SQL:1999, this idea of variable-length traversal paths in a query can be expressed using
something called recursive common table expressions (the WITH RECURSIVE syntax).
[Example 2-5](#fig_graph_sql_query) shows the same query—finding the names of people who emigrated from the
US to Europe—expressed in SQL using this technique (supported in PostgreSQL, IBM DB2, Oracle, and
SQL Server). However, the syntax is very clumsy in comparison to Cypher. ##### Example 2-5. The same query as [Example 2-4](#fig_cypher_query), expressed in SQL using recursive common table expressions ```
`WITH`` ``RECURSIVE``

  ``-- in_usa is the set of vertex IDs of all locations within the United States
``  ``in_usa``(``vertex_id``)`` ``AS`` ``(``
      ``SELECT`` ``vertex_id`` ``FROM`` ``vertices`` ``WHERE`` ``properties``-``>``>``'name'`` ``=`` ``'United States'`` `[![1](assets/1.png)](#callout_data_models_and_query_languages_CO4-1)`
    ``UNION``
      ``SELECT`` ``edges``.``tail_vertex`` ``FROM`` ``edges`` `[![2](assets/2.png)](#callout_data_models_and_query_languages_CO4-2)`
        ``JOIN`` ``in_usa`` ``ON`` ``edges``.``head_vertex`` ``=`` ``in_usa``.``vertex_id``
        ``WHERE`` ``edges``.``label`` ``=`` ``'within'``
  ``)``,``

  ``-- in_europe is the set of vertex IDs of all locations within Europe
``  ``in_europe``(``vertex_id``)`` ``AS`` ``(``
      ``SELECT`` ``vertex_id`` ``FROM`` ``vertices`` ``WHERE`` ``properties``-``>``>``'name'`` ``=`` ``'Europe'`` `[![3](assets/3.png)](#callout_data_models_and_query_languages_CO4-3)`
    ``UNION``
      ``SELECT`` ``edges``.``tail_vertex`` ``FROM`` ``edges``
        ``JOIN`` ``in_europe`` ``ON`` ``edges``.``head_vertex`` ``=`` ``in_europe``.``vertex_id``
        ``WHERE`` ``edges``.``label`` ``=`` ``'within'``
  ``)``,``

  ``-- born_in_usa is the set of vertex IDs of all people born in the US
``  ``born_in_usa``(``vertex_id``)`` ``AS`` ``(`` `[![4](assets/4.png)](#callout_data_models_and_query_languages_CO4-4)`
    ``SELECT`` ``edges``.``tail_vertex`` ``FROM`` ``edges``
      ``JOIN`` ``in_usa`` ``ON`` ``edges``.``head_vertex`` ``=`` ``in_usa``.``vertex_id``
      ``WHERE`` ``edges``.``label`` ``=`` ``'born_in'``
  ``)``,``

  ``-- lives_in_europe is the set of vertex IDs of all people living in Europe
``  ``lives_in_europe``(``vertex_id``)`` ``AS`` ``(`` `[![5](assets/5.png)](#callout_data_models_and_query_languages_CO4-5)`
    ``SELECT`` ``edges``.``tail_vertex`` ``FROM`` ``edges``
      ``JOIN`` ``in_europe`` ``ON`` ``edges``.``head_vertex`` ``=`` ``in_europe``.``vertex_id``
      ``WHERE`` ``edges``.``label`` ``=`` ``'lives_in'``
  ``)``

``SELECT`` ``vertices``.``properties``-``>``>``'name'``
``FROM`` ``vertices``
``-- join to find those people who were both born in the US *and* live in Europe
``JOIN`` ``born_in_usa``     ``ON`` ``vertices``.``vertex_id`` ``=`` ``born_in_usa``.``vertex_id`` `[![6](assets/6.png)](#callout_data_models_and_query_languages_CO4-6)`
``JOIN`` ``lives_in_europe`` ``ON`` ``vertices``.``vertex_id`` ``=`` ``lives_in_europe``.``vertex_id``;`
```