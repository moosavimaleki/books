
The sort tool is a great example of a program that does one thing well. It is arguably a better
sorting implementation than most programming languages have in their standard libraries (which do not
spill to disk and do not use multiple threads, even when that would be beneficial). And yet, sort
is barely useful in isolation. It only becomes powerful in combination with the other Unix tools,
such as uniq. 
A Unix shell like bash lets us easily compose these small programs into surprisingly powerful
data processing jobs. Even though many of these programs are written by different groups of people,
they can be joined together in flexible ways. What does Unix do to enable this composability? ### A uniform interface If you expect the output of one program to become the input to another program, that means those
programs must use the same data format—in other words, a compatible interface. If you want to be
able to connect any program’s output to any program’s input, that means that all programs must
use the same input/output interface.