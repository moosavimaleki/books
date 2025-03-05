However, finding good abstractions is very hard. In the field of distributed systems, although there
are many good algorithms, it is much less clear how we should be packaging them into abstractions
that help us keep the complexity of the system at a manageable level. Throughout this book, we will keep our eyes open for good abstractions that allow us to extract
parts of a large system into well-defined, reusable components. ## Evolvability: Making Change Easy 
It’s extremely unlikely that your system’s requirements will remain unchanged forever. They are much more
likely to be in constant flux: you learn new facts, previously unanticipated use cases emerge,
business priorities change, users request new features, new platforms replace old platforms, legal
or regulatory requirements change, growth of the system forces architectural changes, etc. 
In terms of organizational processes, Agile working patterns provide a framework for adapting to
change. The Agile community has also developed technical tools and patterns that are helpful when
developing software in a frequently changing environment, such as test-driven development (TDD) and
refactoring.