"""Tests for the simple graph class."""

from unittest import TestCase
from tempfile import NamedTemporaryFile
from numpy.testing import assert_array_almost_equal, assert_raises, assert_equal
from simple_graph import SimpleDirectedGraph


class SimpleDirectedGraphTest(TestCase):
    """Tests the simple graph."""

    def test_graph_construction_edges(self) -> None:
        """Test for constructing a graph."""

        vertices = [1, 2]
        edges = [(1, 2), (2, 2)]

        sdg = SimpleDirectedGraph(vertices, edges)

        assert_equal(sdg.num_edges, 2)
        assert_equal(sdg.num_vertices, 2)

        assert_equal(sdg.adjacency[0, 0], False)
        assert_equal(sdg.adjacency[1, 1], True)
        assert_equal(sdg.adjacency[0, 1], True)
        assert_equal(sdg.adjacency[1, 0], False)

    def test_raises(self) -> None:
        """Test for raising value errors """
        vertices = [1, 2, 1]
        edges = [(1, 2), (2, 2)]

        assert_raises(ValueError, SimpleDirectedGraph, vertices, edges)

        vertices = [1, 2]
        edges = [(1, 2), (2, 2)]
        assert_raises(ValueError, SimpleDirectedGraph, vertices, edges, edges)

    def test_graph_construction_edges_string(self) -> None:
        """Test for constructing a graph."""

        vertices = ['one', 'two']
        edges = [('one', 'two'), ('two', 'two')]

        sdg = SimpleDirectedGraph(vertices, edges)

        assert_equal(sdg.num_edges, 2)
        assert_equal(sdg.num_vertices, 2)

        assert_equal(sdg.adjacency[0, 0], False)
        assert_equal(sdg.adjacency[1, 1], True)
        assert_equal(sdg.adjacency[0, 1], True)
        assert_equal(sdg.adjacency[1, 0], False)

    def test_hdf5(self) -> None:
        """Test saving and loading from HDF5."""

        vertices = [1, 2]
        edges = [(1, 2), (2, 2)]
        sdg = SimpleDirectedGraph(vertices, edges)

        with NamedTemporaryFile() as file:
            sdg.save_to_hdf5(file.name, 'tmpgroup')
            file.seek(0)
            sdg_hdf5 = SimpleDirectedGraph.fromhdf5(file.name, 'tmpgroup')

            assert_raises(ValueError, SimpleDirectedGraph.fromhdf5, file.name, 'tmpgroup1')

        assert_array_almost_equal(sdg_hdf5.adjacency.toarray(), sdg.adjacency.toarray())
        for vertex_1, vertex_2 in zip(sdg_hdf5.vertices, sdg.vertices):
            assert_equal(vertex_1, vertex_2)

    def test_hdf5_str_vertices(self) -> None:
        """Test saving and loading from HDF5 using string nodes."""

        vertices = ['one', 'two']
        edges = [('one', 'two'), ('two', 'two')]
        sdg = SimpleDirectedGraph(vertices, edges)

        with NamedTemporaryFile() as file:
            sdg.save_to_hdf5(file.name, 'tmpgroup')
            file.seek(0)
            sdg_hdf5 = SimpleDirectedGraph.fromhdf5(file.name, 'tmpgroup')

        assert_array_almost_equal(sdg_hdf5.adjacency.toarray(), sdg.adjacency.toarray())
        for vertex_1, vertex_2 in zip(sdg_hdf5.vertices, sdg.vertices):
            assert_equal(vertex_1, vertex_2)
