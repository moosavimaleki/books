*  In virtualized environments, a virtual machine can be suspended (pausing the execution of all
processes and saving the contents of memory to disk) and resumed (restoring the contents of
memory and continuing execution). This pause can occur at any time in a process’s execution and can
last for an arbitrary length of time. This feature is sometimes used for live migration of
virtual machines from one host to another without a reboot, in which case the length of the pause
depends on the rate at which processes are writing to memory
[[67](ch08.html#Clark2005ud)]. *  On end-user devices such as laptops, execution may also be suspended and resumed arbitrarily, e.g.,
when the user closes the lid of their laptop. *  
When the operating system context-switches to another thread, or when the hypervisor switches to a
different virtual machine (when running in a virtual machine), the currently running thread can be
paused at any arbitrary point in the code. In the case of a virtual machine, the CPU time spent in
other virtual machines is known as steal time. If the machine is under heavy load—i.e., if
there is a long queue of threads waiting to run—it may take some time before the paused thread
gets to run again.