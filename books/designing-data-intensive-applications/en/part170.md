
If you want to update the value for an existing key in a B-tree, you search for the leaf page
containing that key, change the value in that page, and write the page back to disk (any references
to that page remain valid). If you want to add a new key, you need to find the page whose range
encompasses the new key and add it to that page. If there isn’t enough free space in the page to
accommodate the new key, it is split into two half-full pages, and the parent page is updated to
account for the new subdivision of key ranges—see
[Figure 3-7](#fig_storage_b_tree_split).[ii](ch03.html#idm140605778235856) ![ddia 0307](assets/ddia_0307.png) ###### Figure 3-7. Growing a B-tree by splitting a page. This algorithm ensures that the tree remains balanced: a B-tree with n keys always has a depth
of O(log n). Most databases can fit into a B-tree that is three or four levels deep, so
you don’t need to follow many page references to find the page you are looking for. (A four-level
tree of 4 KB pages with a branching factor of 500 can store up to 256 TB.)