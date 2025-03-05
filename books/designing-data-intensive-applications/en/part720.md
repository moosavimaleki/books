Returning to the marriage analogy, before saying “I do,” you and your bride/groom have the freedom
to abort the transaction by saying “No way!” (or something to that effect). However, after saying “I
do,” you cannot retract that statement. If you faint after saying “I do” and you don’t hear the
minister speak the words “You are now husband and wife,” that doesn’t change the fact that the
transaction was committed. When you recover consciousness later, you can find out whether you are
married or not by querying the minister for the status of your global transaction ID, or you can
wait for the minister’s next retry of the commit request (since the retries will have continued
throughout your period of unconsciousness). ### Coordinator failure 
We have discussed what happens if one of the participants or the network fails during 2PC: if any of
the prepare requests fail or time out, the coordinator aborts the transaction; if any of the
commit or abort requests fail, the coordinator retries them indefinitely. However, it is less
clear what happens if the coordinator crashes.