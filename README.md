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

# display info
sdg.print_num_edges()
sdg.print_num_vertices()

# plot out degree
sdg = SimpleDirectedGraph(vertices, edges)
sdg.plot_outdegrees()

# export to hdf5
sdg.save_to_hdf5('my_graph.hd5', 'graph1')

# load from hdf5
sdg2 = SimpleDirectedGraph.fromhdf5('my_graph.hd5', 'graph1')
sdg2.plot_outdegrees('mygraph.png')

```
![image](https://user-images.githubusercontent.com/17587387/130370379-ab395ddd-5dbd-4dd5-8c83-5a47f0a61e2e.png)

# Unit tests 
``` make pytest``` results in 

![image](https://user-images.githubusercontent.com/17587387/130530907-abd03990-ff4f-4691-8332-cafdddd5564d.png)

