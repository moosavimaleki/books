MapReduce in general is described in more detail in [Chapter 10](ch10.html#ch_batch). For now, we’ll just briefly
discuss MongoDB’s use of the model. MapReduce is neither a declarative query language nor a fully imperative query API, but somewhere
in between: the logic of the query is expressed with snippets of code, which are called repeatedly
by the processing framework. It is based on the map (also known as collect) and reduce (also
known as fold or inject) functions that exist in many functional programming languages. 
To give an example, imagine you are a marine biologist, and you add an observation record to your
database every time you see animals in the ocean. Now you want to generate a report saying how many
sharks you have sighted per month. In PostgreSQL you might express that query like this: ```
`SELECT`` ``date_trunc``(``'month'``,`` ``observation_timestamp``)`` ``AS`` ``observation_month``,`` `[![1](assets/1.png)](#callout_data_models_and_query_languages_CO2-1)`
       ``sum``(``num_animals``)`` ``AS`` ``total_animals``
``FROM`` ``observations``
``WHERE`` ``family`` ``=`` ``'Sharks'``
``GROUP`` ``BY`` ``observation_month``;`
```