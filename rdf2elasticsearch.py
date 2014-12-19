#!/usr/bin/env python
from rdflib import Graph
import json
from elasticsearch import Elasticsearch

#initialize graph object
g = Graph()
#initialize ElasticSearch object
es = Elasticsearch()

#load and parse a notation-three file as for example. Use any Linked Data serialization format supported by rdflib here
g.parse('myfile.n3',format='n3')
#convert to json-ld and load as python dictionary
jsonld = json.loads(g.serialize(format='json-ld'))

#loop through the entities in the serialized graph
for doc in jsonld:
    #load into index!
	es.index(index="myindex", doc_type="mydoctype", body=doc)