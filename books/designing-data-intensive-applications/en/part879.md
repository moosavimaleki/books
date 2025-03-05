### Specialization for different domains While the extensibility of being able to run arbitrary code is useful, there are also many common
cases where standard processing patterns keep reoccurring, and so it is worth having reusable
implementations of the common building blocks. Traditionally, MPP databases have served the needs of
business intelligence analysts and business reporting, but that is just one among many domains in
which batch processing is used. 
Another domain of increasing importance is statistical and numerical algorithms, which are needed
for machine learning applications such as classification and recommendation systems. Reusable
implementations are emerging: for example, Mahout implements various algorithms for machine learning
on top of MapReduce, Spark, and Flink, while MADlib implements similar functionality inside a
relational MPP database (Apache HAWQ) [[54](ch10.html#Cohen2009fv)]. 
Also useful are spatial algorithms such as k-nearest neighbors
[[80](ch10.html#Blazevski2016ve)], which searches for items
that are close to a given item in some multi-dimensional space—a kind of similarity search.
Approximate search is also important for genome analysis algorithms, which need to find strings that
are similar but not identical [[81](ch10.html#White2016ua)].