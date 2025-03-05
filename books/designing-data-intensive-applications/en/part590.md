You can imagine the request-handling loop looking something like this: ```
`while` `(``true``)` `{`
    `request` `=` `getIncomingRequest``();`

    `// Ensure that the lease always has at least 10 seconds remaining`
    `if` `(``lease``.``expiryTimeMillis` `-` `System``.``currentTimeMillis``()` `<` `10000``)` `{`
        `lease` `=` `lease``.``renew``();`
    `}`

    `if` `(``lease``.``isValid``())` `{`
        `process``(``request``);`
    `}`
`}`
``` What’s wrong with this code? Firstly, it’s relying on synchronized clocks: the expiry time on the
lease is set by a different machine (where the expiry may be calculated as the current time plus 30
seconds, for example), and it’s being compared to the local system clock. If the clocks are out of
sync by more than a few seconds, this code will start doing strange things. Secondly, even if we change the protocol to only use the local monotonic clock, there is another
problem: the code assumes that very little time passes between the point that it checks the time
(System.currentTimeMillis()) and the time when the request is processed (process(request)).
Normally this code runs very quickly, so the 10 second buffer is more than enough to ensure that the
lease doesn’t expire in the middle of processing a request.