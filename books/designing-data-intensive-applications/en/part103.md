
Finally, declarative languages often lend themselves to parallel execution. Today, CPUs are getting
faster by adding more cores, not by running at significantly higher clock speeds than before
[[31](ch02.html#Sutter2005us)].
Imperative code is very hard to parallelize across multiple cores and multiple machines, because it
specifies instructions that must be performed in a particular order. Declarative languages have a
better chance of getting faster in parallel execution because they specify only the pattern of the
results, not the algorithm that is used to determine the results. The database is free to use a
parallel implementation of the query language, if appropriate
[[32](ch02.html#Hellerstein2010uq)]. ## Declarative Queries on the Web 
The advantages of declarative query languages are not limited to just databases. To illustrate the
point, let’s compare declarative and imperative approaches in a completely different environment: a
web browser. 
Say you have a website about animals in the ocean. The user is currently viewing the page on sharks,
so you mark the navigation item “Sharks” as currently selected, like this: