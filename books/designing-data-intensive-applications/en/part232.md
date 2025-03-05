Serialization is unfortunately also used in the context of transactions (see [Chapter 7](ch07.html#ch_transactions)),
with a completely different meaning. To avoid overloading the word we’ll stick with encoding in
this book, even though serialization is perhaps a more common term. As this is such a common problem, there are a myriad different libraries and encoding formats to
choose from. Let’s do a brief overview. ## Language-Specific Formats 
Many programming languages come with built-in support for encoding in-memory objects into byte
sequences. For example, Java has java.io.Serializable
[[1](ch04.html#JavaSerializable)], Ruby has Marshal
[[2](ch04.html#RubyAPI)], Python has pickle
[[3](ch04.html#PythonPickle)],
and so on. Many third-party libraries also exist, such as Kryo for Java
[[4](ch04.html#JavaKryo)]. These encoding libraries are very convenient, because they allow in-memory objects to be saved and
restored with minimal additional code. However, they also have a number of deep problems: *  The encoding is often tied to a particular programming language, and reading the data in another
language is very difficult. If you store or transmit data in such an encoding, you are committing
yourself to your current programming language for potentially a very long time, and precluding
integrating your systems with those of other organizations (which may use different languages).