Record the conflict in an explicit data structure that preserves all information, and write
application code that resolves the conflict at some later time (perhaps by prompting the user). ### Custom conflict resolution logic 
As the most appropriate way of resolving a conflict may depend on the application, most multi-leader
replication tools let you write conflict resolution logic using application code. That code may be
executed on write or on read: On write 
As soon as the database system detects a conflict in the log of replicated changes, it calls the
conflict handler. For example, Bucardo allows you to write a snippet of Perl for this purpose.
This handler typically cannot prompt a user—it runs in a background process and it must execute
quickly. On read 
When a conflict is detected, all the conflicting writes are stored. The next time the data is
read, these multiple versions of the data are returned to the application. The application may
prompt the user or automatically resolve the conflict, and write the result back to the database.
CouchDB works this way, for example.