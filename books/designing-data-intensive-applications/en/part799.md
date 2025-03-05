
In Unix, that interface is a file (or, more precisely, a file descriptor). A file is just an ordered
sequence of bytes. Because that is such a simple interface, many different things can be represented
using the same interface: an actual file on the filesystem, a communication channel to another
process (Unix socket, stdin, stdout), a device driver (say /dev/audio or /dev/lp0), a socket
representing a TCP connection, and so on. It’s easy to take this for granted, but it’s actually
quite remarkable that these very different things can share a uniform interface, so they can easily
be plugged together.[ii](ch10.html#idm140605758320400) 
By convention, many (but not all) Unix programs treat this sequence of bytes as ASCII text. Our log
analysis example used this fact: awk, sort, uniq, and head all treat their input file
as a list of records separated by the \n (newline, ASCII 0x0A) character. The choice of \n is
arbitrary—arguably, the ASCII record separator 0x1E would have been a better choice, since it’s
intended for this purpose [[14](ch10.html#Duncan2009ts)]—but in any case, the fact that
all these programs have standardized on using the same record separator allows them to interoperate.