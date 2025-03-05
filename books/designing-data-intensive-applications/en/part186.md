### Full-text search and fuzzy indexes 
All the indexes discussed so far assume that you have exact data and allow you to query for exact
values of a key, or a range of values of a key with a sort order. What they don’t allow you to do is
search for similar keys, such as misspelled words. Such fuzzy querying requires different
techniques. 
For example, full-text search engines commonly allow a search for one word to be expanded to include
synonyms of the word, to ignore grammatical variations of words, and to search for occurrences of words
near each other in the same document, and support various other features that depend on linguistic analysis
of the text. To cope with typos in documents or queries, Lucene is able to search text for words
within a certain edit distance (an edit distance of 1 means that one letter has been added, removed,
or replaced) [[37](ch03.html#McCandless2011wp)].