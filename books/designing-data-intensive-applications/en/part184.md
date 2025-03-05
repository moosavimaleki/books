
The most common type of multi-column index is called a concatenated index, which simply combines
several fields into one key by appending one column to another (the index definition specifies in
which order the fields are concatenated). This is like an old-fashioned paper phone book, which
provides an index from (lastname, firstname) to phone number. Due to the sort order, the index
can be used to find all the people with a particular last name, or all the people with a particular
lastname-firstname combination. However, the index is useless if you want to find all the people
with a particular first name. Multi-dimensional indexes are a more general way of querying several columns at once, which is
particularly important for geospatial data. For example, a restaurant-search website may have a
database containing the latitude and longitude of each restaurant. When a user is looking at the
restaurants on a map, the website needs to search for all the restaurants within the rectangular map
area that the user is currently viewing. This requires a two-dimensional range query like the
following: