4.  Meanwhile, client 2 wants to add ham to the cart, unaware that client 1 just added flour.
Client 2 received the two values [milk] and [eggs] from the server in the last response, so
the client now merges those values and adds ham to form a new value, [eggs, milk, ham]. It
sends that value to the server, along with the previous version number 2. The server detects that
version 2 overwrites [eggs] but is concurrent with [milk, flour], so the two remaining
values are [milk, flour] with version 3, and [eggs, milk, ham] with version 4. 5.  Finally, client 1 wants to add bacon. It previously received [milk, flour] and [eggs] from
the server at version 3, so it merges those, adds bacon, and sends the final value
[milk, flour, eggs, bacon] to the server, along with the version number 3. This overwrites
[milk, flour] (note that [eggs] was already overwritten in the last step) but is concurrent
with [eggs, milk, ham], so the server keeps those two concurrent values.