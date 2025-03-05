Since the problem that the two models were solving is still so relevant today, it’s worth briefly
revisiting this debate in today’s light. ### The network model 
The network model was standardized by a committee called the Conference on Data Systems Languages
(CODASYL) and implemented by several different database vendors; it is also known as the
CODASYL model [[16](ch02.html#Knowles1984tm)]. The CODASYL model was a generalization of the hierarchical model. In the tree structure of the
hierarchical model, every record has exactly one parent; in the network model, a record could have
multiple parents. For example, there could be one record for the "Greater Seattle Area" region,
and every user who lived in that region could be linked to it. This allowed many-to-one and
many-to-many relationships to be modeled. 
The links between records in the network model were not foreign keys, but more like pointers in a
programming language (while still being stored on disk). The only way of accessing a record was to
follow a path from a root record along these chains of links. This was called an access path.