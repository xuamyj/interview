from code.graphs.representations.adjacency_list import AdjListGraph
from code.graphs.representations.matrix import MatrixGraph
from code.graphs.representations.pointers import Graph

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
        # graphObj = graphClass()
        # self.testEmptyGraph(graphObj)
        # graphObj = graphClass()
        # self.testOneNodeGraph(graphObj)
        # graphObj = graphClass()
        # self.testTwoNodeGraph(graphObj)
        # graphObj = graphClass()
        # self.testCompleteGraph(graphObj, 4)
        # graphObj = graphClass()
        # self.testCompleteGraph(graphObj, 5)
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
    def testEmptyGraph(self, graphObj):
        print 'Running empty graph test.'
        assert graphObj.getAllNodeVals() == set()
        assert graphObj.getAllEdgeVals() == set()

    def testOneNodeGraph(self, graphObj):
        print 'Running one node graph test.'
        graphObj.addNode(0)
        assert graphObj.getAllNodeVals() == set([0])
        assert graphObj.getAllEdgeVals() == set()
        assert graphObj.getNeighbors(0) == set()

    def testTwoNodeGraph(self, graphObj):
        print 'Running two node graph test.'
        graphObj.addNode(0)
        graphObj.addNode(1)
        graphObj.addEdge(1, 0)
        assert graphObj.getAllNodeVals() == set([0, 1])
        assert graphObj.getAllEdgeVals() == set([(1, 0)])
        assert graphObj.getNeighbors(0) == set()
        assert graphObj.getNeighbors(1) == set([0])

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
            assert graphObj.getNeighbors(0) == set(range(numNodes))
            for j in range(numNodes/2):
                assert graphObj.isEdge(i, j) == True

    def testResizeGraph(self, graphObj):
        print 'Running resize graph test.'
        pass

    def testDirectedGraph(self, graphObj):
        print 'Running directed graph test.'
        pass

    def testUndirectedGraph(self, graphObj):
        print 'Running undirected graph test.'
        pass

    def testDisconnectedGraph(self, graphObj):
        print 'Running disconnected graph test.'
        pass

    def testLonelyNodeGraph(self, graphObj):
        print 'Running lonely node graph test.'
        pass



