class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def __str__(self) -> list:
        return f"BST - {BST.inorder_traversal(self.root)}"

# ----------------------------------------------------------------------------

    @staticmethod
    def inorder_traversal(node):
        ret_me = []
        if node.left:
            ret_me.extend(BST.inorder_traversal(node.left))
        ret_me.append(node.val)
        if node.right:
            ret_me.extend(BST.inorder_traversal(node.right))
        return ret_me

# ----------------------------------------------------------------------------

    def insert(self, val):
        return BST._insert(self.root, val)

    @staticmethod
    def _insert(node:Node, val):
        if val == node.val:
            return False
        elif val < node.val:
            if node.left:
                return BST._insert(node.left, val)
            node.left = Node(val)
        elif val > node.val:
            if node.right:
                return BST._insert(node.right, val)
            node.right = Node(val)
        return True

# ----------------------------------------------------------------------------

    @staticmethod
    def get_predesc(node:Node):
        if node.left:
            return BST._get_predesc(node.left)
        return node.val

    @staticmethod
    def _get_predesc(node:Node):
        if node.right:
            return BST._get_predesc(node.right)
        return node.val

# ----------------------------------------------------------------------------

    def find(self, val):
        ''' if found return (Node, True) else return (None, False) '''
        return BST._find(self.root, val)

    @staticmethod
    def _find(node:Node, val):
        if val == node.val:
            return (node, True)
        elif val < node.val:
            if node.left:
                return BST._find(node.left, val)
        elif val > node.val:
            if node.right:
                return BST._find(node.right, val)
        return (None, False)

# ----------------------------------------------------------------------------

    def insert_all(self, *vals):
        for val in vals:
            self.insert(val=val)

# ----------------------------------------------------------------------------

    def delete(self, val):
        self.root = BST._delete(self.root, val)

    @staticmethod
    def _delete(node, val):
        if node is None:
            return node
        elif val < node.val:
            node.left = BST._delete(node.left, val)
        elif val > node.val:
            node.right = BST._delete(node.right, val)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.val = BST.get_predesc(node)
                node.left = BST._delete(node.left, node.val)
            
        return node

# ----------------------------------------------------------------------------



b = BST(41)
b.insert_all(20, 65, 11, 29, 50, 26)
print(b)


b.delete(29)
print(b)
