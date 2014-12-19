rdf2elasticsearch
=================

Small-scale elasticsearch-loader script in python for RDF: Linked Data. Simplest form, just for experimental purposes - you'd want to customize the way the index is loaded in any other case.

Install:
No need, just run python rdf2elasticsearch.py. Make sure to update your settings: what file to parse, what index name to use and what document type to use.

Dependencies:
Python
RDFlib (easy_install rdflib, requires python-setuptools to be installed)
python elasticsearch package (pip install elasticsearch)
