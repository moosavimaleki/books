[ii](ch01.html#idm140605786070912-marker) A term borrowed from electronic
engineering, where it describes the number of logic gate inputs that are attached to another gate’s
output. The output needs to supply enough current to drive all the attached inputs. In transaction
processing systems, we use it to describe the number of requests to other services that we need to
make in order to serve one incoming request. [iii](ch01.html#idm140605785971184-marker) In an ideal world, the running time of a
batch job is the size of the dataset divided by the throughput. In practice, the running time is often
longer, due to skew (data not being spread evenly across worker processes) and needing to wait for the
slowest task to complete. ##### References [[1](ch01.html#Stonebraker2005ux-marker)] Michael Stonebraker and Uğur Çetintemel:
“[‘One Size
Fits All’: An Idea Whose Time Has Come and Gone](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.68.9136&rep=rep1&type=pdf),” at 21st International Conference
on Data Engineering (ICDE), April 2005. [[2](ch01.html#Heimerdinger1992vn-marker)] Walter L. Heimerdinger and Charles B. Weinstock:
“[A Conceptual Framework for System Fault
Tolerance](http://www.sei.cmu.edu/reports/92tr033.pdf),” Technical Report CMU/SEI-92-TR-033, Software Engineering Institute, Carnegie
Mellon University, October 1992.