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

# construct graph class instance
sdg = SimpleDirectedGraph(vertices, edges)

# display info
sdg.print_num_edges()
sdg.print_num_vertices()

# plot out degree
sdg.plot_outdegrees('mygraph.png')

```
![image](https://user-images.githubusercontent.com/17587387/130370379-ab395ddd-5dbd-4dd5-8c83-5a47f0a61e2e.png)

The example output is eg.:
```                                                                      
The graph has 95211 (unique) edges.
The graph has 1000 (unique) vertices.
```
## Export / import from HDF5
```python

# export to hdf5
sdg.save_to_hdf5('my_graph.hd5', 'graph1')

# load from hdf5
sdg2 = SimpleDirectedGraph.fromhdf5('my_graph.hd5', 'graph1')
```

# Unit tests 
``` make pytest``` results in 

![image](https://user-images.githubusercontent.com/17587387/130530907-abd03990-ff4f-4691-8332-cafdddd5564d.png)

