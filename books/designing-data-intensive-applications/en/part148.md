# Chapter 3. Storage and Retrieval

# Chapter 3. Storage and Retrieval Wer Ordnung hält, ist nur zu faul zum Suchen. (If you keep things tidily ordered, you’re just too lazy to go searching.) German proverb ![](assets/ch03-map-ebook.png) 
On the most fundamental level, a database needs to do two things: when you give it some data, it
should store the data, and when you ask it again later, it should give the data back to you. In [Chapter 2](ch02.html#ch_datamodels) we discussed data models and query languages—i.e., the format in which you (the
application developer) give the database your data, and the mechanism by which you can ask for it
again later. In this chapter we discuss the same from the database’s point of view: how we can store
the data that we’re given, and how we can find it again when we’re asked for it. Why should you, as an application developer, care how the database handles storage and retrieval
internally? You’re probably not going to implement your own storage engine from scratch, but you
do need to select a storage engine that is appropriate for your application, from the many that
are available. In order to tune a storage engine to perform well on your kind of workload, you need
to have a rough idea of what the storage engine is doing under the hood.