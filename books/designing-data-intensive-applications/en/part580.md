
Part of the problem is that incorrect clocks easily go unnoticed. If a machine’s CPU is defective or
its network is misconfigured, it most likely won’t work at all, so it will quickly be noticed and
fixed. On the other hand, if its quartz clock is defective or its NTP client is misconfigured, most
things will seem to work fine, even though its clock gradually drifts further and further away from
reality. If some piece of software is relying on an accurately synchronized clock, the result is
more likely to be silent and subtle data loss than a dramatic crash
[[53](ch08.html#Kingsbury2013ti_ch8),
[54](ch08.html#Daily2013te_ch8)]. Thus, if you use software that requires synchronized clocks, it is essential that you also carefully
monitor the clock offsets between all the machines. Any node whose clock drifts too far from the
others should be declared dead and removed from the cluster. Such monitoring ensures that you notice
the broken clocks before they can cause too much damage.