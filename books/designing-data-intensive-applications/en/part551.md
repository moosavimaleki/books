3.  The remote node may have failed (perhaps it crashed or it was powered down). 4.  The remote node may have temporarily stopped responding (perhaps it is experiencing a long
garbage collection pause; see [“Process Pauses”](#sec_distributed_clocks_pauses)), but it will start responding
again later. 5.  The remote node may have processed your request, but the response has been lost on the network
(perhaps a network switch has been misconfigured). 6.  The remote node may have processed your request, but the response has been delayed and will be
delivered later (perhaps the network or your own machine is overloaded). ![ddia 0801](assets/ddia_0801.png) ###### Figure 8-1. If you send a request and don’t get a response, it’s not possible to distinguish whether (a) the request was lost, (b) the remote node is down, or (c) the response was lost. The sender can’t even tell whether the packet was delivered: the only option is for the recipient to
send a response message, which may in turn be lost or delayed. These issues are indistinguishable in
an asynchronous network: the only information you have is that you haven’t received a response yet.
If you send a request to another node and don’t receive a response, it is impossible to tell why.