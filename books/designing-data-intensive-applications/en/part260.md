# Modes of Dataflow 
At the beginning of this chapter we said that whenever you want to send some data to another process
with which you don’t share memory—for example, whenever you want to send data over the network or
write it to a file—you need to encode it as a sequence of bytes. We then discussed a variety of
different encodings for doing this. 
We talked about forward and backward compatibility, which are important for evolvability (making
change easy by allowing you to upgrade different parts of your system independently, and not having
to change everything at once). Compatibility is a relationship between one process that encodes the
data, and another process that decodes it. That’s a fairly abstract idea—there are many ways data can flow from one process to another.
Who encodes the data, and who decodes it? In the rest of this chapter we will explore some of the
most common ways how data flows between processes: