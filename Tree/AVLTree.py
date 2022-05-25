from Binary_Search_Tree import BiTreeNode, BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0     # balance factor

class AVLTree(BST):
    def __init__(self, nums=None):
        BST.__init__(self, nums)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:     # insert g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.rchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s2
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:  # insert g
            p.bf = 0
            c.bf = 0
        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # empty tree
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # if lchild not exist
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild      # node saves the node inserted
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:  # if rchild not exist
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:   # ==
                return

            # update bf
        while node.parent:      # node not empty
            if node.parent.lchild == node:        # from left subtree
                # update node.parent.bf -= 1
                if node.parent.bf < 0:      # -1 -> -2
                    # rotate
                    # see which side deeper
                    g = node.parent.parent     # for linking the subtree after rotation
                    x = node.parent      # root of subtree before rotation
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # link n and g!!!
                elif node.parent.bf > 0:    # 1 -> 0
                    node.parent.bf = 0
                    break
                else:    # 0 -> -1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:             # from right subtree
                # update node.parent.bf += 1
                if node.parent.bf < 0:      # 1 -> 2
                    # rotate
                    # see which side deeper
                    g = node.parent.parent     # for linking the subtree after rotation
                    x = node.parent  # root of subtree before rotation
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    # link n and g!!!
                elif node.parent.bf < 0:    # -1 -> 0
                    node.parent.bf = 0
                    break
                else:    # 0 -> 1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # linking subtree after rotation
            n.parent = g
            if g:                  # g not empty
                if x == g.lchild:
                   g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
