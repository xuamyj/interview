from code.graphs.representations.adjacency_list import AdjListGraph
from code.graphs.representations.matrix import MatrixGraph
from code.graphs.representations.pointers import Graph

from collections import deque # amy says: .append(val) and .popleft()

class GraphRepresentationsTester(object):
    def __init__(self):
        pass

    def runTest(self, testName):
        if testName == 'adjacency_list':
            self.runAdjListGraphTests()
        elif testName == 'matrix':
            self.runMatrixGraphTests()
        elif testName == 'pointers':
            self.runGraphTests()

    def runAdjListGraphTests(self):
        graphClass = AdjListGraph
        self.verifyGraph(graphClass)

    def runMatrixGraphTests(self):
        graphClass = MatrixGraph
        self.verifyGraph(graphClass)

    def runGraphTests(self):
        graphClass = Graph
        self.verifyGraph(graphClass)

    def verifyGraph(self, graphClass):
        graphObj = graphClass()
        self.testEmptyGraph(graphObj)
        graphObj = graphClass()
        self.testOneNodeGraph(graphObj)
        graphObj = graphClass()
        self.testTwoNodeGraph(graphObj)
        graphObj = graphClass()
        self.testCompleteGraph(graphObj, 4)
        graphObj = graphClass()
        self.testCompleteGraph(graphObj, 5)
        graphObj = graphClass()
        self.testResizeGraph(graphObj)
        graphObj = graphClass()
        self.testDirectedGraph(graphObj)
        graphObj = graphClass()
        self.testUndirectedGraph(graphObj)
        graphObj = graphClass()
        self.testDisconnectedGraph(graphObj)
        graphObj = graphClass()
        self.testLonelyNodeGraph(graphObj)
        print 'Passed all %s tests.' % (graphObj.name)


    # Helper functions
    # ----------------
    def isReachable(self, graphObj, startNodeVal, endNodeVal, maxSteps=None):
        q = deque()
        steps = {}

        q.append(startNodeVal)
        steps[startNodeVal] = 0

        while len(q) > 0:
            currNodeVal = q.popleft()
            if maxSteps and steps[currNodeVal] > maxSteps:
                return False

            if currNodeVal == endNodeVal:
                return True

            for neighborVal in graphObj.getNeighborVals(currNodeVal):
                if neighborVal not in steps:
                    q.append(neighborVal)
                    steps[neighborVal] = steps[currNodeVal] + 1
        return False

    def testEmptyGraph(self, graphObj):
        print 'Running empty graph test.'
        assert graphObj.getAllNodeVals() == set()
        assert graphObj.getAllEdgeVals() == set()

    def testOneNodeGraph(self, graphObj):
        print 'Running one node graph test.'
        graphObj.addNode(0)
        assert graphObj.getAllNodeVals() == set([0])
        assert graphObj.getAllEdgeVals() == set()
        assert graphObj.getNeighborVals(0) == set()

    def testTwoNodeGraph(self, graphObj):
        print 'Running two node graph test.'
        graphObj.addNode(0)
        graphObj.addNode(1)
        graphObj.addEdge(1, 0)
        assert graphObj.getAllNodeVals() == set([0, 1])
        assert graphObj.getAllEdgeVals() == set([(1, 0)])
        assert graphObj.getNeighborVals(0) == set()
        assert graphObj.getNeighborVals(1) == set([0])

    def testCompleteGraph(self, graphObj, numNodes):
        print 'Running complete-%d graph test.' % (numNodes)

        for i in range(numNodes):
            graphObj.addNode(i)
        edgeValSet = set()
        for i in range(numNodes):
            for j in range(numNodes):
                graphObj.addEdge(i, j)
                edgeValSet.add((i, j))

        assert graphObj.getAllNodeVals() == set(range(numNodes))
        assert graphObj.getAllEdgeVals() == edgeValSet
        for i in range(numNodes):
            assert graphObj.getNeighborVals(0) == set(range(numNodes))
            for j in range(numNodes/2):
                assert graphObj.isEdge(i, j) == True

    def testResizeGraph(self, graphObj):
        print 'Running resize graph test.'
        for i in range(21):
            graphObj.addNode(i)
        assert graphObj.getAllNodeVals() == set(range(21))
        assert graphObj.getAllEdgeVals() == set()

    def testDirectedGraph(self, graphObj):
        print 'Running directed graph test.'

        for i in range(1, 7):
            graphObj.addNode(i)
        edges = [
            (1, 6),
            (1, 2),
            (2, 4),
            (2, 3),
            (3, 2),
            (3, 5),
            (5, 4),
        ]
        for edge in edges:
            graphObj.addEdge(edge[0], edge[1])

        assert graphObj.getAllNodeVals() == set(range(1, 7))
        assert graphObj.getAllEdgeVals() == set(edges)
        assert graphObj.getNeighborVals(1) == set([2, 6])
        assert graphObj.getNeighborVals(2) == set([3, 4])
        assert graphObj.getNeighborVals(3) == set([2, 5])
        assert graphObj.getNeighborVals(4) == set()
        assert graphObj.getNeighborVals(5) == set([4])
        for i in range(1, 7):
            assert self.isReachable(graphObj, 1, i) == True
        for i in range(1, 4):
            assert self.isReachable(graphObj, 4, i) == False
        assert self.isReachable(graphObj, 5, 2) == False
        assert self.isReachable(graphObj, 3, 6) == False

    def testUndirectedGraph(self, graphObj):
        print 'Running undirected graph test.'
        for i in range(1, 7):
            graphObj.addNode(i)
        edges = [
            (1, 2),
            (2, 1),
            (1, 3),
            (3, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (4, 5),
            (5, 4),
            (3, 5),
            (5, 3),
            (5, 6),
            (6, 5),
        ]
        for edge in edges:
            graphObj.addEdge(edge[0], edge[1])

        assert graphObj.getAllNodeVals() == set(range(1, 7))
        assert graphObj.getAllEdgeVals() == set(edges)
        assert graphObj.getNeighborVals(5) == set([3, 4, 6])
        assert graphObj.getNeighborVals(6) == set([5])
        for i in range(1, 7):
            for j in range(1, 7):
                assert self.isReachable(graphObj, i, j) == True

    def testDisconnectedGraph(self, graphObj):
        print 'Running disconnected graph test.'
        for i in range(1, 10):
            graphObj.addNode(i)
        edges = [
            (1, 2),
            (2, 1),
            (1, 3),
            (3, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (4, 5),
            (5, 4),
            (3, 5),
            (5, 3),
            (5, 6),
            (6, 5),
            (7, 8),
            (8, 7),
            (8, 9),
            (9, 8),
            (9, 7),
            (7, 9),
        ]
        for edge in edges:
            graphObj.addEdge(edge[0], edge[1])

        assert graphObj.getAllNodeVals() == set(range(1, 10))
        assert graphObj.getAllEdgeVals() == set(edges)
        assert graphObj.getNeighborVals(5) == set([3, 4, 6])
        assert graphObj.getNeighborVals(6) == set([5])
        assert graphObj.getNeighborVals(7) == set([8, 9])
        for i in range(1, 7):
            for j in range(1, 7):
                assert self.isReachable(graphObj, i, j) == True

        for i in range(7, 10):
            for j in range(7, 10):
                assert self.isReachable(graphObj, i, j) == True

        assert self.isReachable(graphObj, 1, 9) == False
        assert self.isReachable(graphObj, 1, 8) == False
        assert self.isReachable(graphObj, 6, 7) == False

    def testLonelyNodeGraph(self, graphObj):
        print 'Running lonely node graph test.'
        for i in range(1, 8):
            graphObj.addNode(i)
        edges = [
            (1, 2),
            (2, 1),
            (1, 3),
            (3, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (4, 5),
            (5, 4),
            (3, 5),
            (5, 3),
            (5, 6),
            (6, 5),
        ]
        for edge in edges:
            graphObj.addEdge(edge[0], edge[1])

        assert graphObj.getAllNodeVals() == set(range(1, 8))
        assert graphObj.getAllEdgeVals() == set(edges)
        assert graphObj.getNeighborVals(5) == set([3, 4, 6])
        assert graphObj.getNeighborVals(6) == set([5])
        assert graphObj.getNeighborVals(7) == set([])
        for i in range(1, 7):
            for j in range(1, 7):
                assert self.isReachable(graphObj, i, j) == True
        for i in range(1, 7):
            assert self.isReachable(graphObj, i, 7) == False

