[![1](assets/1.png)](#co_data_models_and_query_languages_CO2-1) The date_trunc('month', timestamp) function determines the calendar month
containing timestamp, and returns another timestamp representing the beginning of that month. In
other words, it rounds a timestamp down to the nearest month. This query first filters the observations to only show species in the Sharks family, then groups
the observations by the calendar month in which they occurred, and finally adds up the number of
animals seen in all observations in that month. 
The same can be expressed with MongoDB’s MapReduce feature as follows: ```
`db``.``observations``.``mapReduce``(``
    ``function`` ``map``(``)`` ``{`` `[![2](assets/2.png)](#callout_data_models_and_query_languages_CO3-2)`
        ``var`` ``year``  ``=`` ``this``.``observationTimestamp``.``getFullYear``(``)``;``
        ``var`` ``month`` ``=`` ``this``.``observationTimestamp``.``getMonth``(``)`` ``+`` ``1``;``
        ``emit``(``year`` ``+`` ``"-"`` ``+`` ``month``,`` ``this``.``numAnimals``)``;`` `[![3](assets/3.png)](#callout_data_models_and_query_languages_CO3-3)`
    ``}``,``
    ``function`` ``reduce``(``key``,`` ``values``)`` ``{`` `[![4](assets/4.png)](#callout_data_models_and_query_languages_CO3-4)`
        ``return`` ``Array``.``sum``(``values``)``;`` `[![5](assets/5.png)](#callout_data_models_and_query_languages_CO3-5)`
    ``}``,``
    ``{``
        ``query``:`` ``{`` ``family``:`` ``"Sharks"`` ``}``,`` `[![1](assets/1.png)](#callout_data_models_and_query_languages_CO3-1)`
        ``out``:`` ``"monthlySharkReport"`` `[![6](assets/6.png)](#callout_data_models_and_query_languages_CO3-6)`
    ``}``
``)``;`
``` [![1](assets/1.png)](#co_data_models_and_query_languages_CO3-5) The filter to consider only shark species can be specified declaratively (this is a
MongoDB-specific extension to MapReduce).