However, in other ways, MapReduce and its dataflow successors are very different from the fully
declarative query model of SQL. MapReduce was built around the idea of function callbacks: for each
record or group of records, a user-defined function (the mapper or reducer) is called, and that
function is free to call arbitrary code in order to decide what to output. This approach has the
advantage that you can draw upon a large ecosystem of existing libraries to do things like parsing,
natural language analysis, image analysis, and running numerical or statistical algorithms. 
The freedom to easily run arbitrary code is what has long distinguished batch processing systems of
MapReduce heritage from MPP databases (see [“Comparing Hadoop to Distributed Databases”](#sec_batch_mr_vs_db)); although databases have
facilities for writing user-defined functions, they are often cumbersome to use and not well
integrated with the package managers and dependency management systems that are widely used in most
programming languages (such as Maven for Java, npm for JavaScript, and Rubygems for Ruby).