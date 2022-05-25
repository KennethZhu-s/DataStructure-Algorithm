class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, nums=None):
        self.root = None
        if nums:
            for val in nums:
                self.insert_no_rec(val)

    def insert(self, node, val):  # recursive
        if not node:  # if node is empty
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):  # non-recursive method
        p = self.root
        if not p:  # empty tree
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # if lchild not exist
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # if rchild not exist
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if val < node.data:
            return self.query(node.lchild, val)
        if val > node.data:
            return self.query(node.rchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            else:
                return p
        return None

    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):  # case 1: node is leave node
        if not node.parent:  # root node
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:  # node == node.parent.rchild
            node.parent.rchild = None

    def __remove_node_21(self, node):  # case 2.1: node only has 1 lchild
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        if node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # node == node.parent.rchild
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):  # case 2.2: node only has 1 rchild
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        if node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:  # node == node.parent.rchild
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # if not empty
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:  # case 1
                self.__remove_node_1(node)
            elif not node.rchild:  # case 2.1
                self.__remove_node_21(node)
            elif not node.lchild:  # case 2.2
                self.__remove_node_22(node)
            else:  # case 3: node has l and r child
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # then delete min_node, need case 1 and 2 now!
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


# import random

# nums = list(range(500))
# random.shuffle(nums)
#
# tree = BST(nums)
# tree.pre_order(tree.root)
# print("")
# tree.in_order(tree.root)
# print("")
# tree.post_order(tree.root)

# nums = list(range(0, 500, 2))
# random.shuffle(nums)
#
# tree = BST(nums)
# print(tree.query_no_rec(5))

# tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
# tree.pre_order(tree.root)
# print("")
#
# tree.delete(4)
# tree.in_order(tree.root)
