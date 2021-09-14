class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        curNode = self.root
        isFound = False
        while (not isFound):
            if (new_val < curNode.value):
                if (curNode.left):
                    curNode = curNode.left
                else :
                    curNode.left = Node(new_val)
                    isFound = True
            else:
                if (curNode.right):
                    curNode = curNode.right
                else :
                    curNode.right = Node(new_val)
                    isFound = True

        pass

    def search(self, find_val):
        curNode = self.root
        isFound = False
        while (not isFound and curNode):
            if (find_val == curNode.value):
                isFound = True
                break
            if (find_val < curNode.value):
                curNode = curNode.left
            else:
                curNode = curNode.right
        return isFound


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))