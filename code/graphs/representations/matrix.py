class MatrixGraph(object):
    def __init__(self, initSize=10):
        # nodes must be added before edges can be added
        self.matrix = [[0]*initSize for _ in range(initSize)]
        self.valToIndex = {}
        self.indexToVal = {}

        self.numNodes = 0
        self.initSize = initSize

        self.name = 'matrix'

    def addNode(self, val):
        if self.numNodes == self.initSize:
            # resize
            newMatrix = [[0]*(self.initSize*2) for _ in range(self.initSize*2)]
            for i in range(self.initSize):
                for j in range(self.initSize):
                    newMatrix[i][j] = self.matrix[i][j]
            self.matrix = newMatrix
            self.initSize *= 2

        # add node
        self.valToIndex[val] = self.numNodes
        self.indexToVal[self.numNodes] = val
        self.numNodes += 1

    def addEdge(self, startNodeVal, endNodeVal, weight=1):
        if startNodeVal not in self.valToIndex or endNodeVal not in self.valToIndex:
            raise Exception('addEdge(): one or more of the nodes does not exist')
        self.matrix[self.valToIndex[startNodeVal]][self.valToIndex[endNodeVal]] = weight

    def getAllNodeVals(self):
        return set(self.valToIndex.keys())

    # O(numNodes^2)
    def getAllEdgeVals(self):
        allEdgeVals = set()
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                if self.matrix[i][j] != 0:
                    allEdgeVals.add((self.indexToVal[i], self.indexToVal[j]))
        return allEdgeVals

    # easier than adjacency list, O(1)
    def isEdge(self, startNodeVal, endNodeVal):
        return self.matrix[self.valToIndex[startNodeVal]][self.valToIndex[endNodeVal]] != 0

    # harder than adjacency list, O(numNodes)
    def getNeighborVals(self, val):
        neighbors = set()
        for j in range(self.numNodes):
            if self.matrix[self.valToIndex[val]][j] != 0:
                neighbors.add(self.indexToVal[j])
        return neighbors
