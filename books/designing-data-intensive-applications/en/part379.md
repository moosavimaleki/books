*  When a client reads a key, the server returns all values that have not been overwritten, as well
as the latest version number. A client must read a key before writing. *  When a client writes a key, it must include the version number from the prior read, and it must
merge together all values that it received in the prior read. (The response from a write request
can be like a read, returning all current values, which allows us to chain several writes like in
the shopping cart example.) *  When the server receives a write with a particular version number, it can overwrite all values
with that version number or below (since it knows that they have been merged into the new value),
but it must keep all values with a higher version number (because those values are concurrent with
the incoming write). When a write includes the version number from a prior read, that tells us which previous state the
write is based on. If you make a write without including a version number, it is concurrent with all
other writes, so it will not overwrite anything—it will just be returned as one of the values
on subsequent reads.