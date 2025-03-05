
When a data format or schema changes, a corresponding change to application code often needs to
happen (for example, you add a new field to a record, and the application code starts reading
and writing that field). However, in a large application, code changes often cannot happen
instantaneously: *  With server-side applications you may want to perform a  rolling upgrade
(also known as a staged rollout), deploying the new version to a few nodes at a time, checking
whether the new version is running smoothly, and gradually working your way through all the nodes.
This allows new versions to be deployed without service downtime, and thus encourages more
frequent releases and better evolvability. *  With client-side applications you’re at the mercy of the user, who may not install the update for
some time. 
This means that old and new versions of the code, and old and new data formats, may potentially all
coexist in the system at the same time. In order for the system to continue running smoothly, we
need to maintain compatibility in both directions: