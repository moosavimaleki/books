The good news is that a middle ground is possible. Linearizability is not the only way of preserving
causality—there are other ways too. A system can be causally consistent without incurring the
performance hit of making it linearizable (in particular, the CAP theorem does not apply). In fact,
causal consistency is the strongest possible consistency model that does not slow down due to
network delays, and remains available in the face of network failures
[[2](ch09.html#Mahajan2011wz),
[42](ch09.html#Attiya2015dm)]. In many cases, systems that appear to require linearizability in fact only really require causal
consistency, which can be implemented more efficiently. Based on this observation, researchers are
exploring new kinds of databases that preserve causality, with performance and availability
characteristics that are similar to those of eventually consistent systems
[[49](ch09.html#Lloyd2013vf),
[50](ch09.html#Zawirski2013wc),
[51](ch09.html#Bailis2013wl)]. As this research is quite recent, not much of it has yet made its way into production systems, and
there are still challenges to be overcome
[[52](ch09.html#Ajoux2015wh_ch9), [53](ch09.html#Bailis2014tn)].
However, it is a promising direction for future systems.