*  Subtle interactions between the storage engine and the filesystem implementation can lead to bugs
that are hard to track down, and may cause files on disk to be corrupted after a crash
[[15](ch07.html#Pillai2014vx_ch7), [16](ch07.html#Siebenmann2016ua)]. *  Data on disk can gradually become corrupted without this being detected
[[17](ch07.html#Bairavasundaram2008vx)].
If data has been corrupted for some time, replicas and recent backups may also be corrupted. In
this case, you will need to try to restore the data from a historical backup. *  One study of SSDs found that between 30% and 80% of drives develop at least one bad block during
the first four years of operation
[[18](ch07.html#Schroeder2016us)].
Magnetic hard drives have a lower rate of bad sectors, but a higher rate of complete failure than
SSDs. *  If an SSD is disconnected from power, it can start losing data within a few weeks, depending on
the temperature [[19](ch07.html#Allison2015ta)]. In practice, there is no one technique that can provide absolute guarantees. There are only various
risk-reduction techniques, including writing to disk, replicating to remote machines, and
backups—and they can and should be used together. As always, it’s wise to take any theoretical
“guarantees” with a healthy grain of salt.