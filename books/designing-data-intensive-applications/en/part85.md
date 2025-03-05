![ddia 0203](assets/ddia_0203.png) ###### Figure 2-3. The company name is not just a string, but a link to a company entity. Screenshot of linkedin.com. [Figure 2-4](#fig_datamodels_many_to_many) illustrates how these new features require many-to-many
relationships. The data within each dotted rectangle can be grouped into one document, but the
references to organizations, schools, and other users need to be represented as references, and
require joins when queried. ![ddia 0204](assets/ddia_0204.png) ###### Figure 2-4. Extending résumés with many-to-many relationships. ## Are Document Databases Repeating History? 
While many-to-many relationships and joins are routinely used in relational databases, document
databases and NoSQL reopened the debate on how best to represent such relationships in a database.
This debate is much older than NoSQL—in fact, it goes back to the very earliest computerized
database systems. 
The most popular database for business data processing in the 1970s was IBM’s Information
Management System (IMS), originally developed for stock-keeping in the Apollo
space program and first commercially released in 1968
[[13](ch02.html#Long2000wy)].
It is still in use and maintained today, running on OS/390 on IBM mainframes
[[14](ch02.html#Bartlett2013uo)].