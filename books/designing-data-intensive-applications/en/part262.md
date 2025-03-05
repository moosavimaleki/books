This means that a value in the database may be written by a newer version of the code, and
subsequently read by an older version of the code that is still running. Thus, forward
compatibility is also often required for databases. However, there is an additional snag. Say you add a field to a record schema, and the newer code
writes a value for that new field to the database. Subsequently, an older version of the code (which
doesn’t yet know about the new field) reads the record, updates it, and writes it back. In this
situation, the desirable behavior is usually for the old code to keep the new field intact, even
though it couldn’t be interpreted. The encoding formats discussed previously support such preservation of unknown fields, but sometimes you
need to take care at an application level, as illustrated in [Figure 4-7](#fig_encoding_preserve_field). For
example, if you decode a database value into model objects in the application, and later reencode
those model objects, the unknown field might be lost in that translation process. Solving this is
not a hard problem; you just need to be aware of it.