*  Additional pointers have been added to the tree. For example, each leaf page may have references to
its sibling pages to the left and right, which allows scanning keys in order without jumping back
to parent pages. *   B-tree variants such as fractal trees
  [[22](ch03.html#Kuszmaul2014wr)] borrow some log-structured ideas to reduce disk seeks (and they have
  nothing to do with fractals). ## Comparing B-Trees and LSM-Trees 
Even though B-tree implementations are generally more mature than LSM-tree implementations,
LSM-trees are also interesting due to their performance characteristics. As a rule of thumb,
LSM-trees are typically faster for writes, whereas B-trees are thought to be faster for reads
[[23](ch03.html#Athanassoulis2016jk)].
Reads are typically slower on LSM-trees because they have to check several different data structures
and SSTables at different stages of compaction. However, benchmarks are often inconclusive and sensitive to details of the workload. You need to
test systems with your particular workload in order to make a valid comparison. In this section we
will briefly discuss a few things that are worth considering when measuring the performance of a
storage engine.