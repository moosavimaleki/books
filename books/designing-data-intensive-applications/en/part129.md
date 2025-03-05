### The RDF data model 
The Turtle language we used in [Example 2-7](#fig_graph_n3_shorthand) is a human-readable format for RDF data.
Sometimes RDF is also written in an XML format, which does the same thing much more verbosely—see
[Example 2-8](#fig_graph_rdf_xml). Turtle/N3 is preferable as it is much easier on the eyes, and tools like
Apache Jena
[[42](ch02.html#Jena2013)]
can automatically convert between different RDF formats if necessary. ##### Example 2-8. The data of [Example 2-7](#fig_graph_n3_shorthand), expressed using RDF/XML syntax ```
``

  ``
    ``Idaho``
    ``state``
    ``
      ``
        ``United States``
        ``country``
        ``
          ``
            ``North America``
            ``continent``
          ``
        ``
      ``
    ``
  ``

  ``
    ``Lucy``
    ``
  ``
``
``` RDF has a few quirks due to the fact that it is designed for internet-wide data exchange. The
subject, predicate, and object of a triple are often URIs. For example, a predicate might be an URI
such as  or ,
rather than just WITHIN or LIVES_IN. The reasoning behind this design is that you should be able
to combine your data with someone else’s data, and if they attach a different meaning to the word
within or lives_in, you won’t get a conflict because their predicates are actually
 and .