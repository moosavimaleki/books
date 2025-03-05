A secondary index can easily be constructed from a key-value index. The main difference is that keys
are not unique; i.e., there might be many rows (documents, vertices) with the same key. This can be
solved in two ways: either by making each value in the index a list of matching row identifiers (like a
postings list in a full-text index) or by making each key unique by appending a row identifier to
it. Either way, both B-trees and log-structured indexes can be used as secondary indexes. ### Storing values within the index 
The key in an index is the thing that queries search for, but the value can be one of two things:
it could be the actual row (document, vertex) in question, or it could be a reference to the row
stored elsewhere. In the latter case, the place where rows are stored is known as a heap file, and
it stores data in no particular order (it may be append-only, or it may keep track of deleted rows
in order to overwrite them with new data later). The heap file approach is common because it avoids
duplicating data when multiple secondary indexes are present: each index just references a location
in the heap file, and the actual data is kept in one place.