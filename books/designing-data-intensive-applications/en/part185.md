```
`SELECT` `*` `FROM` `restaurants` `WHERE` `latitude`  `>` `51``.``4946` `AND` `latitude`  `<` `51``.``5079`
                            `AND` `longitude` `>` `-``0``.``1162` `AND` `longitude` `<` `-``0``.``1004``;`
``` A standard B-tree or LSM-tree index is not able to answer that kind of query efficiently: it can
give you either all the restaurants in a range of latitudes (but at any longitude), or all the
restaurants in a range of longitudes (but anywhere between the North and South poles), but not both
simultaneously. 
One option is to translate a two-dimensional location into a single number using a space-filling
curve, and then to use a regular B-tree index
[[34](ch03.html#Ramsak2000wm)].
More commonly, specialized spatial indexes such as R-trees are used. For example, PostGIS implements
geospatial indexes as R-trees using PostgreSQL’s Generalized Search Tree indexing facility
[[35](ch03.html#PostGIS2014)].
We don’t have space to describe R-trees in detail here, but there is plenty of literature on them. An interesting idea is that multi-dimensional indexes are not just for geographic locations. For
example, on an ecommerce website you could use a three-dimensional index on the dimensions (red,
green, blue) to search for products in a certain range of colors, or in a database of weather
observations you could have a two-dimensional index on (date, temperature) in order to
efficiently search for all the observations during the year 2013 where the temperature was between
25 and 30℃. With a one-dimensional index, you would have to either scan over all the records from
2013 (regardless of temperature) and then filter them by temperature, or vice versa. A 2D index
could narrow down by timestamp and temperature simultaneously.

This technique is used by HyperDex
[[36](ch03.html#Escriva2012gh)].