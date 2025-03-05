You can even write your own programs and combine them with the tools provided by the operating
system. Your program just needs to read input from stdin and write output to stdout, and it can
participate in data processing pipelines. In the log analysis example, you could write a tool that
translates user-agent strings into more sensible browser identifiers, or a tool that translates IP
addresses into country codes, and simply plug it into the pipeline. The sort program doesn’t care
whether it’s communicating with another part of the operating system or with a program written by
you. However, there are limits to what you can do with stdin and stdout. Programs that need multiple
inputs or outputs are possible but tricky. You can’t pipe a program’s output into a network
connection [[17](ch10.html#DJBTwoFD),
[18](ch10.html#Pike1999ui)].[iii](ch10.html#idm140605758280016) 
If a program directly opens files for reading and writing, or starts another program as a
subprocess, or opens a network connection, then that I/O is wired up by the program itself. It can
still be configurable (through command-line options, for example), but the flexibility of wiring up
inputs and outputs in a shell is reduced.