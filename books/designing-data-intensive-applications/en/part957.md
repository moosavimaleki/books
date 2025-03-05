*  Trading systems need to examine price changes in a financial market and execute trades according
to specified rules. *  Manufacturing systems need to monitor the status of machines in a factory, and quickly identify
the problem if there is a malfunction. *  Military and intelligence systems need to track the activities of a potential aggressor, and raise
the alarm if there are signs of an attack. These kinds of applications require quite sophisticated pattern matching and correlations. However,
other uses of stream processing have also emerged over time. In this section we will briefly compare
and contrast some of these applications. ### Complex event processing Complex event processing (CEP) is an approach developed in the 1990s for analyzing event streams,
especially geared toward the kind of application that requires searching for certain event patterns
[[65](ch11.html#Luckham2006tv),
[66](ch11.html#Perera2015tz)].
Similarly to the way that a regular expression allows you to search for certain patterns of
characters in a string, CEP allows you to specify rules to search for certain patterns of events in
a stream.