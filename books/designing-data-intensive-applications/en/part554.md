Even if network faults are rare in your environment, the fact that faults can occur means that
your software needs to be able to handle them. Whenever any communication happens over a network, it
may fail—there is no way around it. 
If the error handling of network faults is not defined and tested, arbitrarily bad things could
happen: for example, the cluster could become deadlocked and permanently unable to serve requests,
even when the network recovers [[20](ch08.html#Kingsbury2014vi)], or it could even delete all of
your data [[21](ch08.html#Sanfilippo2014ty)].
If software is put in an unanticipated situation, it may do arbitrary unexpected things. Handling network faults doesn’t necessarily mean tolerating them: if your network is normally
fairly reliable, a valid approach may be to simply show an error message to users while your network
is experiencing problems. However, you do need to know how your software reacts to network problems
and ensure that the system can recover from them.