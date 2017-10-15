title: Linked Data & the Semantic Web
published: 2017-10-16
description: Linked Data is the core technology enabling future library systems and the semantic web.
previous: www
next: bibcat

Libraries and cultural heritage organizations are shifting from [MARC21][MRC] 
and XML metadata standards to Linked-Data vocabularies. Library Linked Data 
is an international effort to bring machine-readable data to the web. Based 
on RDF (Resource Description Framework) graphs, Library Linked Data is made 
up a series of statements, called triples, that take the form of 
**subject - predicate - object**. 

## What is a RDF Graph?

A graph data structure is made up nodes (also known as vertices or points) 
with connections between the nodes called edges or directed edges (also referred 
to as arcs or lines)

Graphs are used to describe transportation systems, computer networks, and 
social relationships. Graphs easily support heterogeneous environments with 
different vocabularies that can scale to billions (if not trillions) of nodes 
and edges.

## RDF Linked Data for Libraries
Linked Data in libraries is constructed using [Resource Description Framework (RDF)][RDF] 
graphs, a type of directed graphs, where the nodes are made up of either IRI 
(international resource indicator i.e. URLs or URIs), blank nodes (a type of 
identifier placeholder in a [RDF][RDF] graph), or literal values. Originating 
with the World Wide Web Consortium (W3C) specifications, [RDF][RDF] graphs are built 
using three element statements called triples that model relationships between 
resources, IRIs, and descriptive information.

In a RDF triple, the first element is called a **subject** and represents a 
resource with the second element, the **predicate**, describing an aspect that 
connects to the third element, an **object** made up a value, blank node, or
IRI. One or more these triple statements make up a RDF graph. 


[MRC]: http://www.loc.gov/marc/ 
[RDF]: https://www.w3.org/RDF/
