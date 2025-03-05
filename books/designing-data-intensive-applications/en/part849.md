On the other hand, not all kinds of processing can be sensibly expressed as SQL queries. For
example, if you are building machine learning and recommendation systems, or full-text search
indexes with relevance ranking models, or performing image analysis, you most likely need a more
general model of data processing. These kinds of processing are often very specific to a particular
application (e.g., feature engineering for machine learning, natural language models for machine
translation, risk estimation functions for fraud prediction), so they inevitably require writing
code, not just queries. 
MapReduce gave engineers the ability to easily run their own code over large datasets. If you have
HDFS and MapReduce, you can build a SQL query execution engine on top of it, and indeed this is
what the Hive project did [[31](ch10.html#Thusoo2010hp)]. However, you
can also write many other forms of batch processes that do not lend themselves to being expressed as
a SQL query.