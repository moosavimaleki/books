##### The Byzantine Generals Problem The Byzantine Generals Problem is a generalization of the so-called Two Generals Problem
[[78](ch08.html#Gray1978vv)],
which imagines a situation in which two army generals need to agree on a battle plan. As they
have set up camp on two different sites, they can only communicate by messenger, and the messengers
sometimes get delayed or lost (like packets in a network). We will discuss this problem of
consensus in [Chapter 9](ch09.html#ch_consistency). In the Byzantine version of the problem, there are n generals who need to agree, and their
endeavor is hampered by the fact that there are some traitors in their midst. Most of the generals
are loyal, and thus send truthful messages, but the traitors may try to deceive and confuse the
others by sending fake or untrue messages (while trying to remain undiscovered). It is not known in
advance who the traitors are. Byzantium was an ancient Greek city that later became Constantinople, in the place which is now
Istanbul in Turkey. There isn’t any historic evidence that the generals of Byzantium were any more
prone to intrigue and conspiracy than those elsewhere. Rather, the name is derived from Byzantine
in the sense of excessively complicated, bureaucratic, devious, which was used in politics long
before computers [[79](ch08.html#Palmer2011uh)].
Lamport wanted to choose a nationality that would not offend any readers, and he was advised that
calling it The Albanian Generals Problem was not such a good idea
[[80](ch08.html#LamportPubs)].