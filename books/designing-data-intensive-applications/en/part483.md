For example, to prevent two users concurrently updating the same wiki page, you might try something
like this, expecting the update to occur only if the content of the page hasn’t changed since the
user started editing it: ```
`-- This may or may not be safe, depending on the database implementation`
`UPDATE` `wiki_pages` `SET` `content` `=` `'new content'`
  `WHERE` `id` `=` `1234` `AND` `content` `=` `'old content'``;`
``` If the content has changed and no longer matches 'old content', this update will have no effect,
so you need to check whether the update took effect and retry if necessary. However, if the database
allows the WHERE clause to read from an old snapshot, this statement may not prevent lost updates,
because the condition may be true even though another concurrent write is occurring. Check whether
your database’s compare-and-set operation is safe before relying on it. ### Conflict resolution and replication