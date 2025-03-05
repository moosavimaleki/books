## Human Errors 
Humans design and build software systems, and the operators who keep the systems running are also
human. Even when they have the best intentions, humans are known to be unreliable. For example, one
study of large internet services found that configuration errors by operators were the leading cause
of outages, whereas hardware faults (servers or network) played a role in only 10–25% of outages
[[13](ch01.html#Oppenheimer2003vc)]. How do we make our systems reliable, in spite of unreliable humans? The best systems combine several
approaches: *  Design systems in a way that minimizes opportunities for error. For example, well-designed
abstractions, APIs, and admin interfaces make it easy to do “the right thing” and discourage “the
wrong thing.” However, if the interfaces are too restrictive people will work around them,
negating their benefit, so this is a tricky balance to get right. *  Decouple the places where people make the most mistakes from the places where they can cause
failures. In particular, provide fully featured non-production sandbox environments where
people can explore and experiment safely, using real data, without affecting real users.