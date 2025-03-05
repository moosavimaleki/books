Even databases with the same data model often don’t make it easy to get data out of one and into
the other. This lack of integration leads to Balkanization of data. ### Separation of logic and wiring 
Another characteristic feature of Unix tools is their use of standard input (stdin) and standard
output (stdout). If you run a program and don’t specify anything else, stdin comes from the
keyboard and stdout goes to the screen. However, you can also take input from a file and/or
redirect output to a file. Pipes let you attach the stdout of one process to the stdin of
another process (with a small in-memory buffer, and without writing the entire intermediate data
stream to disk). 
A program can still read and write files directly if it needs to, but the Unix approach works best
if a program doesn’t worry about particular file paths and simply uses stdin and stdout. This
allows a shell user to wire up the input and output in whatever way they want; the program doesn’t
know or care where the input is coming from and where the output is going to. (One could say this is
a form of loose coupling, late binding [[15](ch10.html#KayOxymoron)], or inversion of control
[[16](ch10.html#Fowler2005tp)].) Separating the input/output wiring from the
program logic makes it easier to compose small tools into bigger systems.