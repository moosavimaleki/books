*  We can save space in pages by not storing the entire key, but abbreviating it. Especially in pages
on the interior of the tree, keys only need to provide enough information to act as boundaries
between key ranges. Packing more keys into a page allows the tree to have a higher branching
factor, and thus fewer levels.[iii](ch03.html#idm140605778198240) *  In general, pages can be positioned anywhere on disk; there is nothing requiring pages with
nearby key ranges to be nearby on disk. If a query needs to scan over a large part of the key
range in sorted order, that page-by-page layout can be inefficient, because a disk seek may be
required for every page that is read. Many B-tree implementations therefore try to lay out the
tree so that leaf pages appear in sequential order on disk. However, it’s difficult to maintain
that order as the tree grows. By contrast, since LSM-trees rewrite large segments of the storage
in one go during merging, it’s easier for them to keep sequential keys close to each other on disk.