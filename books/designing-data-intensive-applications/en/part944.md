
No matter how the state changes, there was always a sequence of events that caused those changes.
Even as things are done and undone, the fact remains true that those events occurred. The key idea
is that mutable state and an append-only log of immutable events do not contradict each other: they
are two sides of the same coin. The log of all changes, the changelog, represents the evolution of
state over time. 
If you are mathematically inclined, you might say that the application state is what you get when
you integrate an event stream over time, and a change stream is what you get when you differentiate
the state by time, as shown in [Figure 11-6](#fig_stream_integral)
[[49](ch11.html#Hyde2016), [50](ch11.html#Gupta1999uz),
[51](ch11.html#Griffin1995gr)].
The analogy has limitations (for example, the second derivative of state does not seem to be
meaningful), but it’s a useful starting point for thinking about data. ![ddia 1106](assets/ddia_1106.png) ###### Figure 11-6. The relationship between the current application state and an event stream.