from code.graphs.representations.pointers import Graph

import heapq # amy says: h = []; heappush(h, (1, 'x')); heappop(h)

class Dijkstra(object):
    def __init__(self):
        self.name = 'dijkstras'

        self.YELLOW = 'yellow'
        self.GREEN = 'green'

    # returns the values in an list [startNodeVal, ..., endNodeVal]
    def shortestPath(self, graph, startNodeVal, endNodeVal):
        pq = []
        startNode = graph.nodeMap[startNodeVal]
        endNode = graph.nodeMap[endNodeVal]

        # enqueue startNodeVal
        startNode.color = self.YELLOW
        startNode.weight = 0
        heapq.heappush(pq, (0, startNode))

        while len(pq) > 0:
            # process each node
            currNode = heapq.heappop(pq)[1]
            currNode.color = self.GREEN

            if currNode == endNode:
                break

            for edge in currNode.outEdges:
                neighborNode = edge.endNode
                calcWeight = currNode.weight + edge.weight

                if not neighborNode.color:
                    self.setPrevForEnqueue(neighborNode, calcWeight, currNode)
                    heapq.heappush(pq, (calcWeight, neighborNode))

                elif neighborNode.color == self.YELLOW and neighborNode.weight > calcWeight:
                    # re-enqueue
                    pq.remove((neighborNode.weight, neighborNode))
                    self.setPrevForEnqueue(neighborNode, calcWeight, currNode)
                    heapq.heappush(pq, (calcWeight, neighborNode))

        return self.tracePath(endNode)

    def setPrevForEnqueue(self, node, weight, prevNode):
        node.color = self.YELLOW
        node.weight = weight
        node.prevNode = prevNode

    def tracePath(self, currNode):
        reversePath = []
        while (currNode.prevNode):
            reversePath.append(currNode.val)
            currNode = currNode.prevNode
        reversePath.append(currNode.val)
        return reversePath[::-1]
