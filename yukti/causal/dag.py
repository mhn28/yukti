
import networkx as nx

class CausalDAG:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, cause, effect):
        self.graph.add_edge(cause, effect)

    def nodes(self):
        return list(self.graph.nodes)

    def edges(self):
        return list(self.graph.edges)

    def parents(self, node):
        return list(self.graph.predecessors(node))

    def children(self, node):
        return list(self.graph.successors(node))

    def is_dag(self):
        return nx.is_directed_acyclic_graph(self.graph)
