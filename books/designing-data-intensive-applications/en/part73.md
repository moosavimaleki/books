It can take a lot of effort to master just one data model (think how many books there are on
relational data modeling). Building software is hard enough, even when working with just one data
model and without worrying about its inner workings. But since the data model has such a profound
effect on what the software above it can and can’t do, it’s important to choose one that is
appropriate to the application. In this chapter we will look at a range of general-purpose data models for data storage and
querying (point 2 in the preceding list). In particular, we will compare the relational model,
the document model, and a few graph-based data models. We will also look at various query languages
and compare their use cases. In [Chapter 3](ch03.html#ch_storage) we will discuss how storage engines work; that is,
how these data models are actually implemented (point 3 in the list).