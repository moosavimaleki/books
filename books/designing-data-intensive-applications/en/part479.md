```
`UPDATE` `counters` `SET` `value` `=` `value` `+` `1` `WHERE` `key` `=` `'foo'``;`
``` 
Similarly, document databases such as MongoDB provide atomic operations for making local
modifications to a part of a JSON document, and Redis provides atomic operations for modifying data
structures such as priority queues. Not all writes can easily be expressed in terms of atomic
operations—for example, updates to a wiki page involve arbitrary text
editing[viii](ch07.html#idm140605762119856)—but in
situations where atomic operations can be used, they are usually the best choice. 
Atomic operations are usually implemented by taking an exclusive lock on the object when it is read
so that no other transaction can read it until the update has been applied. This technique is
sometimes known as cursor stability [[36](ch07.html#Mukherjee2013uw), [37](ch07.html#Hilker2013vy)].
Another option is to simply force all atomic operations to be executed on a single thread. 
Unfortunately, object-relational mapping frameworks make it easy to accidentally write code that
performs unsafe read-modify-write cycles instead of using atomic operations provided by the
database [[38](ch07.html#Wiger2010vv)]. That’s not a problem if you know what you are doing, but it is
potentially a source of subtle bugs that are difficult to find by testing.