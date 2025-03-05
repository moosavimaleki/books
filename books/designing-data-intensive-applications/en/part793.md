### Chain of commands versus custom program Instead of the chain of Unix commands, you could write a simple program to do the same
thing. For example, in Ruby, it might look something like this: ```
`counts`` ``=`` ``Hash``.``new``(``0``)`` `[![1](assets/1.png)](#callout_batch_processing_CO2-1)`

``File``.``open``(``'/var/log/nginx/access.log'``)`` ``do`` ``|``file``|``
  ``file``.``each`` ``do`` ``|``line``|``
    ``url`` ``=`` ``line``.``split``[``6``]`` `[![2](assets/2.png)](#callout_batch_processing_CO2-2)`
    ``counts``[``url``]`` ``+=`` ``1`` `[![3](assets/3.png)](#callout_batch_processing_CO2-3)`
  ``end``
``end``

``top5`` ``=`` ``counts``.``map``{``|``url``,`` ``count``|`` ``[``count``,`` ``url``]`` ``}``.``sort``.``reverse``[``0``.``.``.``5``]`` `[![4](assets/4.png)](#callout_batch_processing_CO2-4)`
``top5``.``each``{``|``count``,`` ``url``|`` ``puts`` ``"``#{``count``}`` ``#{``url``}``"`` ``}`` `[![5](assets/5.png)](#callout_batch_processing_CO2-5)
``` [![1](assets/1.png)](#co_batch_processing_CO2-1) counts is a hash table that keeps a counter for the number of times we’ve seen each URL. A
counter is zero by default. [![2](assets/2.png)](#co_batch_processing_CO2-2) From each line of the log, we take the URL to be the seventh whitespace-separated field (the
array index here is 6 because Ruby’s arrays are zero-indexed). [![3](assets/3.png)](#co_batch_processing_CO2-3) Increment the counter for the URL in the current line of the log. [![4](assets/4.png)](#co_batch_processing_CO2-4) Sort the hash table contents by counter value (descending), and take the top five entries.