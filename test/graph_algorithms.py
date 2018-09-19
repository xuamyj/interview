from code.graphs.representations.pointers import Graph
from code.graphs.algorithms.dijkstras import Dijkstra
from code.graphs.algorithms.kruskals import Kruskal

class GraphAlgorithmsTester(object):
    def __init__(self):
        pass

    def runTest(self, testName):
        if testName == 'dijkstras':
            self.runDijstraTests()
        elif testName == 'kruskals':
            self.runKruskalTests()

    def runDijstraTests(self):
        dObj = Dijkstra()

        largeGraphObj = self.makeLargeDijkGraph()
        assert dObj.shortestPath(largeGraphObj, 1, 13) == [1, 2, 3, 5, 9, 8, 7, 6, 10, 11, 12, 13]
        largeGraphObj = self.makeLargeDijkGraph()
        assert dObj.shortestPath(largeGraphObj, 3, 5) == [3, 5]
        smallGraphObj = self.makeSmallGraph()
        assert dObj.shortestPath(smallGraphObj, 1, 2) == [1, 2]
        smallGraphObj = self.makeSmallGraph()
        assert dObj.shortestPath(smallGraphObj, 2, 3) == [2, 1, 3]
        smallGraphObj = self.makeSmallGraph()
        assert dObj.shortestPath(smallGraphObj, 3, 1) == [3, 1]
        smallGraphObj = self.makeSmallGraph()
        assert dObj.shortestPath(smallGraphObj, 1, 1) == [1]

        print 'Passed all %s tests.' % (dObj.name)

    def runKruskalTests(self):
        kObj = Kruskal()

        largeGraphObj = self.makeLargeKruskalGraph()
        assert kObj.minSpanningTree(largeGraphObj) == set([(1, 2), (3, 2), (6, 7), (6, 1), (4, 3), (8, 6), (5, 3)])
        smallGraphObj = self.makeSmallGraph()
        assert kObj.minSpanningTree(smallGraphObj) == set([(1, 2), (1, 3)])

        print 'Passed all %s tests.' % (kObj.name)

    def makeLargeDijkGraph(self):
        largeGraphObj = Graph()
        for i in range(1, 14):
            largeGraphObj.addNode(i)
        edges = [
            (1, 2, 1),
            (2, 3, 1),
            (3, 4, 1),
            (4, 5, 1),
            (5, 9, 1),
            (6, 7, 1),
            (7, 8, 1),
            (8, 9, 1),
            (6, 10, 1),
            (10, 11, 1),
            (11, 12, 1),
            (12, 13, 1),
            (2, 6, 9),
            (3, 7, 8),
            (4, 8, 7),
            (7, 11, 5),
            (8, 12, 7),
            (9, 13, 9),
            (3, 5, 2),
        ]
        reverseEdges = [(e[1], e[0], e[2]) for e in edges]
        edges += reverseEdges
        for e in edges:
            largeGraphObj.addEdge(e[0], e[1], e[2])
        return largeGraphObj

    def makeSmallGraph(self):
        smallGraphObj = Graph()
        smallGraphObj.addNode(1)
        smallGraphObj.addNode(2)
        smallGraphObj.addNode(3)
        edges = [
            (1, 2, 1),
            (2, 3, 19),
            (3, 1, 10),
        ]
        reverseEdges = [(e[1], e[0], e[2]) for e in edges]
        edges += reverseEdges
        for e in edges:
            smallGraphObj.addEdge(e[0], e[1], e[2])
        return smallGraphObj

    def makeLargeKruskalGraph(self):
        largeGraphObj = Graph()
        for i in range(1, 9):
            largeGraphObj.addNode(i)
        edges = [
            (1, 2, 1),
            (2, 3, 2),
            (3, 4, 5),
            (4, 5, 7),
            (1, 3, 3),
            (3, 5, 5),
            (1, 6, 9),
            (1, 7, 10),
            (6, 7, 2),
            (6, 8, 8),
        ]
        reverseEdges = [(e[1], e[0], e[2]) for e in edges]
        edges += reverseEdges
        for e in edges:
            largeGraphObj.addEdge(e[0], e[1], e[2])
        return largeGraphObj
