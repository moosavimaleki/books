## Triple-Stores and SPARQL 
The triple-store model is mostly equivalent to the property graph model, using different words to
describe the same ideas. It is nevertheless worth discussing, because there are various tools and
languages for triple-stores that can be valuable additions to your toolbox for building
applications. 
In a triple-store, all information is stored in the form of very simple three-part statements:
(subject, predicate, object). For example, in the triple (Jim, likes, bananas), Jim is
the subject, likes is the predicate (verb), and bananas is the object. The subject of a triple is equivalent to a vertex in a graph. The object is one of two things: 1.  A value in a primitive datatype, such as a string or a number. In that case,
the predicate and object of the triple are equivalent to the key and value of a property on the
subject vertex. For example, (lucy, age, 33) is like a vertex lucy with properties
{"age":33}.