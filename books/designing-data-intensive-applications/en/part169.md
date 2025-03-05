One page is designated as the root of the B-tree; whenever you want to look up a key in the index,
you start here. The page contains several keys and references to child pages.
Each child is responsible for a continuous range of keys, and the keys between the references indicate
where the boundaries between those ranges lie. In the example in [Figure 3-6](#fig_storage_b_tree), we are looking for the key 251, so we know that we need to
follow the page reference between the boundaries 200 and 300. That takes us to a similar-looking
page that further breaks down the 200–300 range into subranges. Eventually we get down to a
page containing individual keys (a leaf page), which either contains the value for each key
inline or contains references to the pages where the values can be found. 
The number of references to child pages in one page of the B-tree is called the branching factor.
For example, in [Figure 3-6](#fig_storage_b_tree) the branching factor is six. In practice, the branching
factor depends on the amount of space required to store the page references and the range
boundaries, but typically it is several hundred.