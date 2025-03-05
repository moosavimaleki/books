*  Test thoroughly at all levels, from unit tests to whole-system integration tests and manual tests
[[3](ch01.html#Yuan2014va)].
Automated testing is widely used, well understood, and especially valuable for covering corner
cases that rarely arise in normal operation. *  Allow quick and easy recovery from human errors, to minimize the impact in the case of a failure.
For example, make it fast to roll back configuration changes, roll out new code gradually (so that
any unexpected bugs affect only a small subset of users), and provide tools to recompute data (in
case it turns out that the old computation was incorrect). *  
Set up detailed and clear monitoring, such as performance metrics and error rates.
In other engineering disciplines this is referred to as telemetry. (Once a rocket has left the
ground, telemetry is essential for tracking what is happening, and for understanding failures
[[14](ch01.html#Marz2013wq)].)
Monitoring can show us early warning signals and allow us to check whether any assumptions or
constraints are being violated. When a problem occurs, metrics can be invaluable in diagnosing the
issue.