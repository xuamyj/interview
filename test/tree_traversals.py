from code.trees.traversals.binary_tree import BinaryTree
from code.trees.traversals.binary_tree import BinaryTreeNode

class TreeTraversalsTester(object):
    def __init__(self):
        self.emptyTree = None
        self.oneNodeTree = self.generateOneNodeTree()
        self.twoNodeTree = self.generateTwoNodeTree()
        self.threeNodeTree = self.generateThreeNodeTree()
        self.balancedTree = self.generateBalancedTree()
        self.veryUnbalancedTree = self.generateVeryUnbalancedTree()
        self.derpyTree = self.generateDerpyTree()

    def runTest(self, testName):
        self.runOrderTests(testName)

    def runOrderTests(self, testName):
        allTrees = [
            self.threeNodeTree,
            self.balancedTree,
            self.veryUnbalancedTree,
            self.derpyTree,
        ]
        for tree in allTrees:
            print 'Here is your tree:'
            tree.indentPrint()

            print 'What is the %s traversal of this tree?' % (testName)
            userAnswer = [int(x) for x in raw_input().split()]
            correctAnswer = self.runSpecificTest(tree, testName)

            while userAnswer != correctAnswer:
                print 'Try again: %s traversal of this tree?' % (testName)
                userAnswer = [int(x) for x in raw_input().split()]
            print 'Okay, good.'

        print 'All done with %s.' % (testName)

    def runSpecificTest(self, tree, testName):
        if testName == 'inorder':
            return tree.inorder()
        elif testName == 'preorder':
            return tree.preorder()
        elif testName == 'postorder':
            return tree.postorder()
        elif testName == 'bfs':
            return tree.bfs()

    # Helper functions
    # ----------------
    def generateOneNodeTree(self):
        root = BinaryTreeNode(2, None, None)
        return BinaryTree(root)

    def generateTwoNodeTree(self):
        left = BinaryTreeNode(10, None, None)
        root = BinaryTreeNode(1, left, None)
        return BinaryTree(root)

    def generateThreeNodeTree(self):
        left = BinaryTreeNode(2, None, None)
        right = BinaryTreeNode(3, None, None)
        root = BinaryTreeNode(1, left, right)
        return BinaryTree(root)

    def generateBalancedTree(self):
        leftLeft = BinaryTreeNode(8, None, None)
        leftRight = BinaryTreeNode(0, None, None)
        rightLeft = BinaryTreeNode(3, None, None)
        rightRight = BinaryTreeNode(11, None, None)
        left = BinaryTreeNode(6, leftLeft, leftRight)
        right = BinaryTreeNode(4, rightLeft, rightRight)
        root = BinaryTreeNode(2, left, right)
        return BinaryTree(root)

    def generateVeryUnbalancedTree(self):
        seven = BinaryTreeNode(7, None, None)
        six = BinaryTreeNode(6, seven, None)
        five = BinaryTreeNode(5, None, six)
        four = BinaryTreeNode(4, None, five)
        three = BinaryTreeNode(3, four, None)
        two = BinaryTreeNode(2, three, None)
        root = BinaryTreeNode(1, two, None)
        return BinaryTree(root)

    def generateDerpyTree(self):
        eleven = BinaryTreeNode(11, None, None)
        seven = BinaryTreeNode(7, eleven, None)
        eight = BinaryTreeNode(8, None, None)
        five = BinaryTreeNode(5, seven, eight)
        four = BinaryTreeNode(4, None, None)
        two = BinaryTreeNode(2, four, five)
        twelve = BinaryTreeNode(12, None, None)
        nine = BinaryTreeNode(9, None, twelve)
        ten = BinaryTreeNode(10, None, None)
        six = BinaryTreeNode(6, nine, ten)
        three = BinaryTreeNode(3, None, six)
        root = BinaryTreeNode(1, two, three)
        return BinaryTree(root, skipFillTree=False)

