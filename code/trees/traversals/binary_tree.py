from collections import deque # amy says: .append(val) and .popleft()


class BinaryTreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root, skipFillTree=True):
        self.root = root
        self.skipFillTree = skipFillTree

    def indentPrint(self):
        if self.skipFillTree:
            self.indentPrintHelper(self.root, '')
        else:
            copy = self.deepCopy()
            self.fillTree(copy, self.height(copy))
            self.indentPrintHelper(copy, '')

    def bfs(self):
        resultList = []
        self.bfsHelper(self.root, resultList)
        return resultList

    def inorder(self):
        resultList = []
        self.inorderHelper(self.root, resultList)
        return resultList

    def preorder(self):
        resultList = []
        self.preorderHelper(self.root, resultList)
        return resultList

    def postorder(self):
        resultList = []
        self.postorderHelper(self.root, resultList)
        return resultList

    # Helper functions
    # ----------------

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def deepCopyHelper(self, original, copy):
        if not original:
            return
        copy.val = original.val
        if original.left:
            copy.left = BinaryTreeNode(None, None, None)
            self.deepCopyHelper(original.left, copy.left)
        if original.right:
            copy.right = BinaryTreeNode(None, None, None)
            self.deepCopyHelper(original.right, copy.right)

    def deepCopy(self):
        copy = BinaryTreeNode(None, None, None)
        self.deepCopyHelper(self.root, copy) # amy says: is there a way to do this using just returns?
        return copy

    def fillTree(self, node, height):
        if height <= 1:
            return

        if not node.left:
            node.left = BinaryTreeNode('-', None, None)
        if not node.right:
            node.right = BinaryTreeNode('-', None, None)

        self.fillTree(node.left, height - 1)
        self.fillTree(node.right, height - 1)

    def indentPrintHelper(self, node, indent):
        if not node:
            return

        self.indentPrintHelper(node.right, indent + '   ')
        print indent, node.val
        self.indentPrintHelper(node.left, indent + '   ')

    def bfsHelper(self, node, passByRefList):
        q = deque()
        if self.root:
            q.append(self.root)

        while len(q) > 0:
            node = q.popleft()
            passByRefList.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def inorderHelper(self, node, passByRefList):
        if not node:
            return

        self.inorderHelper(node.left, passByRefList)
        passByRefList.append(node.val)
        self.inorderHelper(node.right, passByRefList)

    def preorderHelper(self, node, passByRefList):
        if not node:
            return

        passByRefList.append(node.val)
        self.preorderHelper(node.left, passByRefList)
        self.preorderHelper(node.right, passByRefList)

    def postorderHelper(self, node, passByRefList):
        if not node:
            return

        self.postorderHelper(node.left, passByRefList)
        self.postorderHelper(node.right, passByRefList)
        passByRefList.append(node.val)
