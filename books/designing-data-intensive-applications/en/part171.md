### Making B-trees reliable 
The basic underlying write operation of a B-tree is to overwrite a page on disk with new data. It is
assumed that the overwrite does not change the location of the page; i.e., all references to that
page remain intact when the page is overwritten. This is in stark contrast to log-structured indexes
such as LSM-trees, which only append to files (and eventually delete obsolete files) but never
modify files in place. You can think of overwriting a page on disk as an actual hardware operation. On a magnetic hard
drive, this means moving the disk head to the right place, waiting for the right position on the
spinning platter to come around, and then overwriting the appropriate sector with new data. On SSDs,
what happens is somewhat more complicated, due to the fact that an SSD must erase and rewrite
fairly large blocks of a storage chip at a time
[[19](ch03.html#Goossaert2014wj)].