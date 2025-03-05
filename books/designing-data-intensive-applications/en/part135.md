
Cypher and SPARQL jump in right away with SELECT, but Datalog takes a small step at a time. We
define rules that tell the database about new predicates: here, we define two new predicates,
within_recursive and migrated. These predicates aren’t triples stored in the database, but
instead they are derived from data or from other rules. Rules can refer to other rules, just like
functions can call other functions or recursively call themselves. Like this, complex queries can be
built up a small piece at a time. In rules, words that start with an uppercase letter are variables, and predicates are matched like
in Cypher and SPARQL. For example, name(Location, Name) matches the triple
name(namerica, 'North America') with variable bindings
Location = namerica and Name = 'North America'. A rule applies if the system can find a match for all predicates on the righthand side of the
:- operator. When the rule applies, it’s as though the lefthand side of the :- was added to the
database (with variables replaced by the values they matched).