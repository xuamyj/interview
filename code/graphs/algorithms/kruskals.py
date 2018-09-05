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
        edges = graph.getAllEdges().sort(key=lambda edge: edge.weight)
        for edge in edges:
            startNode = edge.startNode
            endNode = edge.endNode

            if self.clusterMap[startNode] != self.clusterMap[endNode]:
                clusterMap[startNode] = self.clusterMap[endNode] = clusterMap[startNode].union(self.clusterMap[endNode])
                mst.add((edge.startNode.val, edge.endNode.val))
                numClusters -= 1

            # optimization
            if numClusters == 1:
                break

        return mst
