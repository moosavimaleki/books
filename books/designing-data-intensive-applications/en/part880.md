Batch processing engines are being used for distributed execution of algorithms from an increasingly
wide range of domains. As batch processing systems gain built-in functionality and high-level
declarative operators, and as MPP databases become more programmable and flexible, the two are
beginning to look more alike: in the end, they are all just systems for storing and processing data. # Summary In this chapter we explored the topic of batch processing. We started by looking at Unix tools such
as awk, grep, and sort, and we saw how the design philosophy of those tools is carried forward
into MapReduce and more recent dataflow engines. Some of those design principles are that inputs are
immutable, outputs are intended to become the input to another (as yet unknown) program, and complex
problems are solved by composing small tools that “do one thing well.” In the Unix world, the uniform interface that allows one program to be composed with another is
files and pipes; in MapReduce, that interface is a distributed filesystem. We saw that dataflow
engines add their own pipe-like data transport mechanisms to avoid materializing intermediate state
to the distributed filesystem, but the initial input and final output of a job is still usually
HDFS.