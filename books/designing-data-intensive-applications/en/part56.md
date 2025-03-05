Even though they are specific to a particular application, scalable architectures are nevertheless
usually built from general-purpose building blocks, arranged in familiar patterns. In this book we
discuss those building blocks and patterns. # Maintainability 
It is well known that the majority of the cost of software is not in its initial development, but in
its ongoing maintenance—fixing bugs, keeping its systems operational, investigating failures,
adapting it to new platforms, modifying it for new use cases, repaying technical debt, and adding
new features. 
Yet, unfortunately, many people working on software systems dislike maintenance of so-called
legacy systems—perhaps it involves fixing other people’s mistakes, or working with platforms
that are now outdated, or systems that were forced to do things they were never intended for. Every
legacy system is unpleasant in its own way, and so it is difficult to give general recommendations
for dealing with them. 
However, we can and should design software in such a way that it will hopefully minimize pain during
maintenance, and thus avoid creating legacy software ourselves. To this end, we will pay particular
attention to three design principles for software systems: