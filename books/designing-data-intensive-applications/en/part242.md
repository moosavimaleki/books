![ddia 0403](assets/ddia_0403.png) ###### Figure 4-3. Example record encoded using Thrift’s CompactProtocol. Finally, Protocol Buffers (which has only one binary encoding format) encodes the same data as shown
in [Figure 4-4](#fig_encoding_protobuf). It does the bit packing slightly differently, but is otherwise very
similar to Thrift’s CompactProtocol. Protocol Buffers fits the same record in 33 bytes. ![ddia 0404](assets/ddia_0404.png) ###### Figure 4-4. Example record encoded using Protocol Buffers. One detail to note: in the schemas shown earlier, each field was marked either required or optional, but
this makes no difference to how the field is encoded (nothing in the binary data indicates whether a
field was required). The difference is simply that required enables a runtime check that fails if
the field is not set, which can be useful for catching bugs. ### Field tags and schema evolution 
We said previously that schemas inevitably need to change over time. We call this schema
evolution. How do Thrift and Protocol Buffers handle schema changes while keeping backward and
forward compatibility?