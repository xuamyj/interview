from code.graphs.representations.pointers import Graph

class Kruskal(object):
    def __init__(self):
        self.name = 'kruskals'

    # returns the edges as a set of val tuples
    def minSpanningTree(self, graph):
        # initialize map from node to cluster
        self.clusterMap = {}
        for node in graph.getAllNodes():
            self.clusterMap[node] = set([node])

        # for optimization
        numClusters = len(self.clusterMap)

        mst = set()
        edges = sorted(graph.getAllEdges(), key=lambda edge: edge.weight)
        for edge in edges:
            startNode = edge.startNode
            endNode = edge.endNode

            if self.clusterMap[startNode] != self.clusterMap[endNode]:
                result = self.clusterMap[startNode].union(self.clusterMap[endNode])
                for node in result:
                    self.clusterMap[node] = result
                mst.add((edge.startNode.val, edge.endNode.val))
                numClusters -= 1

            # optimization
            if numClusters == 1:
                break

        return mst
