#!/usr/bin/env python

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : [],
          "g" : []
        }

edges = []

for k, v in graph.iteritems():
   for i in v:
      edges.append((k, i))

#print edges

def find_isolated_nodes(graph):
   return [k for k, v in graph.iteritems() if not v]

print find_isolated_nodes(graph)
