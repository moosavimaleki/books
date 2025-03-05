If you want to guarantee that there will be no editing conflicts, the application must obtain a lock
on the document before a user can edit it. If another user wants to edit the same document, they
first have to wait until the first user has committed their changes and released the lock. This
collaboration model is equivalent to single-leader replication with transactions on the leader. However, for faster collaboration, you may want to make the unit of change very small (e.g., a single
keystroke) and avoid locking. This approach allows multiple users to edit simultaneously, but it also brings
all the challenges of multi-leader replication, including requiring conflict resolution
[[32](ch05.html#Kleppmann2016ve)]. ## Handling Write Conflicts 
The biggest problem with multi-leader replication is that write conflicts can occur, which means
that conflict resolution is required. For example, consider a wiki page that is simultaneously being edited by two users, as shown in
[Figure 5-7](#fig_replication_write_conflict). User 1 changes the title of the page from A to B, and user 2
changes the title from A to C at the same time. Each user’s change is successfully applied to their
local leader. However, when the changes are asynchronously replicated, a conflict is detected
[[33](ch05.html#Clement2011wc)].
This problem does not occur in a single-leader database.