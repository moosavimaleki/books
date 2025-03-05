In particular, there is a big difference between storage engines that are optimized for
transactional workloads and those that are optimized for analytics. We will explore that distinction
later in [“Transaction Processing or Analytics?”](#sec_storage_analytics), and in [“Column-Oriented Storage”](#sec_storage_column) we’ll discuss a
family of storage engines that is optimized for analytics. However, first we’ll start this chapter by talking about storage engines that are used in the kinds
of databases that you’re probably familiar with: traditional relational databases, and also most
so-called NoSQL databases. We will examine two families of storage engines: log-structured storage
engines, and page-oriented storage engines such as B-trees. # Data Structures That Power Your Database 
Consider the world’s simplest database, implemented as two Bash functions: ```
`#!/bin/bash`

db_set `()` `{`
    `echo` `"``$1``,``$2``"` >> database
`}`

db_get `()` `{`
    grep `"^``$1``,"` database `|` sed -e `"s/^``$1``,//"` `|` tail -n 1
`}`
``` 
These two functions implement a key-value store. You can call db_set key value, which will store
key and value in the database. The key and value can be (almost) anything you like—for
example, the value could be a JSON document. You can then call db_get key, which looks up the most
recent value associated with that particular key and returns it.