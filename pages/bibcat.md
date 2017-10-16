title: BIBCAT - Catalog Pull Platform
published: 2017-10-16
description: BIBCAT open-source project drives the Catalog Pull Platform, a newer way of developing library applications
previous: linked-data-semantic-web

## History
In 2014 the Library of Congress issued an RFQ for a BIBFRAME "search and display" 
system to highlight BIBFRAME. Aaron Schmidt of [Influx Library User Experience]() 
and Jeremy Nelson were awarded the contract with the Library of Congress. 
Together with additional help of Mike Stabile, resulted in BIBCAT - a BIBFRAME Catalog - 
which was a lightweight catalog web application that indexes BIBFRAME 1.0 Linked Data 
into Elasticsearch. 

When the Library of Congress released BIBFRAME 2.0 in April of 2016, the tools for 
converting MARC records to these modified or new BIBFRAME classes and properties were missing.
BIBCAT was modified to provide preliminary support for BIBFRAME 2.0 with its use in two
Linked Data projects; the development of a MARC-to-BIBFRAME Linked Data publishing project for
the Colorado Alliance of Research Libraries and a new DP.LA service hub for Colorado 
and Wyoming.

Currently, BIBCAT is available for installing with the Python package manager PIP 
(i.e. `pip install bibcat`) or from source code hosted on Github at 
[https://github.com/KnowledgeLinks/bibcat.git](https://github.com/KnowledgeLinks/bibcat.git).

## Goldrush BIBCAT
In it's second development iteration, the new Alliance [Goldrush BIBCAT](https://bibcat.coalliance.org/) 
service publish converted MARC21 records the Alliance
uses in their Gold Rush Comparison service
to the web in a format that Google and other search engines can use to index the site. 
The overarching goal of the project was an effort to improve the search ranking of materials 
in Alliance's member libraries catalogs. All source code is open-sourced licensed and available
on Github at []().
 
## Plains2Peaks DP.LA service hub.
In 2016 the State of Library of Colorado started an effort to provide a 
[DP.LA](https://dp.la) service hub for states of Colorado and Wyoming. 
This project uses BIBCAT to transform different formats and vocabularies 
from multiple sources including Denver Public Library's RDF Dublin Core, 
Colorado College and University of Wyoming MODS metadata, and a metadata 
provided as custom Comma-Separated-Value file from the History Colorado museum 
into BIBFRAME 2.0 entities stored in a triplestore.

BIBCAT uses RDF-based rules, based upon [RDF Mapping Language](https://rml.io) to 
ingest these different types of sources while allowing for easy customization and 
modification through simple editing of RDF turtle MAP file. 

