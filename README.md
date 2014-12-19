rdf2elasticsearch
=================

Small-scale elasticsearch-loader script in python for RDF: Linked Data. Simplest form, just for experimental purposes - you'd want to customize the way the index is loaded in any other case.

Install:
No need, just run python rdf2elasticsearch.py. Make sure to update your settings: what file to parse, what index name to use and what document type to use. Be careful not to load too large datasets: the script and the libraries it depends on, are not built to scale. Query your data from a grown up triple store or divide between several files if your data exceeds more than about 100 Mb or so (not quite sure what the limits of RDFlib are here).

Dependencies:
- ElasticSearch
- Python
- RDFlib (easy_install rdflib, requires python-setuptools to be installed)
- python elasticsearch package (pip install elasticsearch)
