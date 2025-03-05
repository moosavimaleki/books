Operability Make it easy for operations teams to keep the system running smoothly. Simplicity Make it easy for new engineers to understand the system, by removing as much complexity as
possible from the system. (Note this is not the same as simplicity of the user interface.) Evolvability Make it easy for engineers to make changes to the system in the future, adapting it for unanticipated
use cases as requirements change. Also known as extensibility, modifiability, or
plasticity. As previously with reliability and scalability, there are no easy solutions for achieving these goals.
Rather, we will try to think about systems with operability, simplicity, and evolvability in mind. ## Operability: Making Life Easy for Operations 
It has been suggested that “good operations can often work around the limitations of bad (or
incomplete) software, but good software cannot run reliably with bad operations”
[[12](ch01.html#Kreps2012td_ch1)]. While some aspects of operations can
and should be automated, it is still up to humans to set up that automation in the first place and
to make sure it’s working correctly.