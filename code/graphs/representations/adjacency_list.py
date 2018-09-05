class AdjListGraph(object):
    def __init__(self):
        # nodes must be added before edges can be added
        self.adjList = {}

        self.name = 'adjacency_list'

    def addNode(self, val):
        self.adjList[val] = []

    def addEdge(self, startNodeVal, endNodeVal, weight=1):
        if startNodeVal not in self.adjList or endNodeVal not in self.adjList:
            raise Exception('addEdge(): one or more of the nodes does not exist')
        self.adjList[startNodeVal].append(endNodeVal)

    def getAllNodeVals(self):
        return set(self.adjList.keys())

    # O(numEdges)
    def getAllEdgeVals(self):
        allEdgeVals = set()
        for startNodeVal in self.adjList:
            for endNodeVal in self.adjList[startNodeVal]:
                allEdgeVals.add((startNodeVal, endNodeVal))
        return allEdgeVals

    # harder than matrix, O(neighbors)
    def isEdge(self, startNodeVal, endNodeVal):
        return endNodeVal in self.adjList[startNodeVal]

    # easier than matrix, O(1)
    def getNeighborVals(self, val):
        return set(self.adjList[val])
