class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.outEdges = set()

        # for bfs
        self.visited = False

        # for dijkstra's
        self.color = None
        self.weight = None
        self.prevNode = None


    def addOutEdge(self, edge):
        self.outEdges.add(edge)

    def setVisited(self, visited):
        self.visited = visited

    def setColor(self, color):
        self.color = color


class GraphEdge(object):
    def __init__(self, startNode, endNode, weight=0):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = weight


class Graph(object):
    def __init__(self):
        # nodes must be added before edges can be added
        self.nodeMap = {}
        self.edgeMap = {}

        self.name = 'pointers'

    def addNode(self, val):
        node = GraphNode(val)
        self.nodeMap[val] = node

    def addEdge(self, startNodeVal, endNodeVal, weight=1):
        if startNodeVal not in self.nodeMap or endNodeVal not in self.nodeMap:
            raise Exception('addEdge(): one or more of the nodes does not exist')
        startNode = self.nodeMap[startNodeVal]
        endNode = self.nodeMap[endNodeVal]
        edge = GraphEdge(startNode, endNode, weight)

        startNode.addOutEdge(edge)
        self.edgeMap[(startNodeVal, endNodeVal)] = edge

    def getAllNodeVals(self):
        return set(self.nodeMap.keys())

    def getAllEdgeVals(self):
        return set(self.edgeMap.keys())

    def isEdge(self, startNodeVal, endNodeVal):
        return (startNodeVal, endNodeVal) in self.edgeMap

    def getNeighborVals(self, val):
        return set([edge.endNode.val for edge in self.nodeMap[val].outEdges])

    # Helper functions for code.graphs.algorithms
    # -------------------------------------------

    def getAllNodes(self):
        return self.nodeMap.values()

    def getAllEdges(self):
        return self.edgeMap.values()

    def getNeighbors(self):
        return [self.nodeMap[edge.endNodeVal] for edge in node.outEdges]
