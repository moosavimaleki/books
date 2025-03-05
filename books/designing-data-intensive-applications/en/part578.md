*  
In virtual machines, the hardware clock is virtualized, which raises additional challenges for
applications that need accurate timekeeping
[[50](ch08.html#VMware2011vm)].
When a CPU core is shared between virtual machines, each VM is paused for tens of milliseconds
while another VM is running. From an application’s point of view, this pause manifests itself as
the clock suddenly jumping forward [[26](ch08.html#Wang2010ja)]. *  If you run software on devices that you don’t fully control (e.g., mobile or embedded devices), you
probably cannot trust the device’s hardware clock at all. Some users deliberately set their
hardware clock to an incorrect date and time, for example to circumvent timing limitations in
games. As a result, the clock might be set to a time wildly in the past or the future. 
It is possible to achieve very good clock accuracy if you care about it sufficiently to invest
significant resources. For example, the MiFID II draft European regulation for financial
institutions requires all high-frequency trading funds to synchronize their clocks to within 100
microseconds of UTC, in order to help debug market anomalies such as “flash crashes” and to help
detect market manipulation
[[51](ch08.html#MiFID2015wn)].