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

![image](https://user-images.githubusercontent.com/17587387/130532657-2891231d-b39f-41fa-ab2d-76f2d5f212b5.png)


The example output is eg.:
```                                                                      
The graph has 95148 (unique) edges.
The graph has 1000 (unique) vertices.
```
## Export / import from HDF5
```python

# export to hdf5
sdg.save_to_hdf5('my_graph.hd5', 'graph1')

# load from hdf5
sdg2 = SimpleDirectedGraph.fromhdf5('my_graph.hd5', 'graph1')
```

## Unit tests 
``` make pytest``` results in 

![image](https://user-images.githubusercontent.com/17587387/130530907-abd03990-ff4f-4691-8332-cafdddd5564d.png)

## Pylint
```
$ make pylint
PYTHONPATH=src/ pylint -rn src/ tests/ 
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

```
$ make mypy
mypy --show-error-codes src/ 
Success: no issues found in 3 source files
```

```
$ make pycodestyle
pycodestyle src/ tests/ 
```
