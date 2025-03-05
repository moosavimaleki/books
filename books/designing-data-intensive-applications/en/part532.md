[x](ch07.html#idm140605761528448-marker) If a
transaction needs to access data that’s not in memory, the best solution may be to abort the
transaction, asynchronously fetch the data into memory while continuing to process other
transactions, and then restart the transaction when the data has been loaded. This approach is
known as anti-caching, as previously mentioned in
[“Keeping everything in memory”](ch03.html#sec_storage_inmemory). [xi](ch07.html#idm140605761509024-marker) Sometimes called
strong strict two-phase locking (SS2PL) to distinguish it from other variants of
2PL. ##### References [[1](ch07.html#Chamberlin1981im-marker)] Donald D. Chamberlin, Morton M. Astrahan, Michael W. Blasgen, et al.:
“[A
History and Evaluation of System R](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.348&rep=rep1&type=pdf),” Communications of the ACM,
volume 24, number 10, pages 632–646, October 1981.
[doi:10.1145/358769.358784](http://dx.doi.org/10.1145/358769.358784) [[2](ch07.html#Gray1976us-marker)] Jim N. Gray, Raymond A. Lorie, Gianfranco R. Putzolu, and Irving L. Traiger:
“[Granularity
of Locks and Degrees of Consistency in a Shared Data Base](http://citeseer.ist.psu.edu/viewdoc/download?doi=10.1.1.92.8248&rep=rep1&type=pdf),” in Modelling in Data
Base Management Systems: Proceedings of the IFIP Working Conference on Modelling in Data Base
Management Systems, edited by G. M. Nijssen, pages
364–394, Elsevier/North Holland Publishing, 1976. Also in Readings in Database Systems, 4th edition, edited by Joseph M.
Hellerstein and Michael Stonebraker, MIT Press, 2005. ISBN: 978-0-262-69314-1