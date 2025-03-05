The theoretical description of an algorithm can declare that certain things are simply assumed not
to happen—and in non-Byzantine systems, we do have to make some assumptions about faults that can
and cannot happen. However, a real implementation may still have to include code to handle the
case where something happens that was assumed to be impossible, even if that handling boils down to
printf("Sucks to be you") and exit(666)—i.e., letting a human operator clean up the mess
[[93](ch08.html#Kreps2013ud)].
(This is arguably the difference between computer science and software engineering.) 
That is not to say that theoretical, abstract system models are worthless—quite the opposite.
They are incredibly helpful for distilling down the complexity of real systems to a manageable set
of faults that we can reason about, so that we can understand the problem and try to solve it
systematically. We can prove algorithms correct by showing that their properties always hold in some
system model.