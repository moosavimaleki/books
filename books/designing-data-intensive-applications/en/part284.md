# Summary In this chapter we looked at several ways of turning data structures into bytes on the network or
bytes on disk. We saw how the details of these encodings affect not only their efficiency, but more
importantly also the architecture of applications and your options for deploying them. In particular, many services need to support rolling upgrades, where a new version of a service is
gradually deployed to a few nodes at a time, rather than deploying to all nodes simultaneously.
Rolling upgrades allow new versions of a service to be released without downtime (thus encouraging
frequent small releases over rare big releases) and make deployments less risky (allowing faulty
releases to be detected and rolled back before they affect a large number of users). These
properties are hugely beneficial for evolvability, the ease of making changes to an application. During rolling upgrades, or for various other reasons, we must assume that different nodes are
running the different versions of our application’s code. Thus, it is important that all data
flowing around the system is encoded in a way that provides backward compatibility (new code can
read old data) and forward compatibility (old code can read new data).