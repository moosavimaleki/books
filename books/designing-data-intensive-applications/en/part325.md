*  When reading something that the user may have modified, read it from the leader; otherwise, read it
from a follower. This requires that you have some way of knowing whether something might have been
modified, without actually querying it. For example, user profile information on a social network
is normally only editable by the owner of the profile, not by anybody else. Thus, a simple
rule is: always read the user’s own profile from the leader, and any other users’ profiles from a
follower. *  If most things in the application are potentially editable by the user, that approach won’t be
effective, as most things would have to be read from the leader (negating the benefit of read
scaling). In that case, other criteria may be used to decide whether to read from the leader. For
example, you could track the time of the last update and, for one minute after the last update, make all
reads from the leader. You could also monitor the replication lag on followers and
prevent queries on any follower that is more than one minute behind the leader.