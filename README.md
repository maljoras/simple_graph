# Simple Graph Class

A simple class for a directed graph. 

* supports HDF5 read/write
* plot out degrees histogram
* unit tests

## Example 

```python

import numpy as np
from simple_graph import SimpleDirectedGraph

# build a random graph
num_vertices = 1000
num_edges = 100000

vertices  = list(range(num_vertices))
from_node = np.random.randint(num_vertices, size=(num_edges,))
to_node = np.random.randint(num_vertices, size=(num_edges,))
edges = list(zip(from_node, to_node))

# plot out degree
sdg = SimpleDirectedGraph(vertices, edges)
sdg.plot_outdegrees()

# export to hdf5
sdg.save_to_hdf5('my_graph.hd5', 'graph1')

```

