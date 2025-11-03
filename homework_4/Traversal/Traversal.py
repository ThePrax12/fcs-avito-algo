class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return True
        current = self.root
        while current is not None:
            if current.value == value:
                return False
            if current.value < value:
                if current.right is None:
                    current.right = TreeNode(value)
                    return True
                current = current.right
            else:
                if current.left is None:
                    current.left = TreeNode(value)
                    return True
                current = current.left

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node=None):
        if node is None:
            return []

        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node=None):
        if node is None:
            return []

        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node=None):
        if node is None:
            return []

        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

    def reverse_inorder(self):
        return self._reverse_inorder(self.root)

    def _reverse_inorder(self, node=None):
        if node is None:
            return []

        return (
            self._reverse_inorder(node.right)
            + [node.value]
            + self._reverse_inorder(node.left)
        )

    def reverse_preorder(self):
        return self._reverse_preorder(self.root)

    def _reverse_preorder(self, node=None):
        if node is None:
            return []

        return (
            [node.value]
            + self._reverse_preorder(node.right)
            + self._reverse_preorder(node.left)
        )

    def reverse_postorder(self):
        return self._reverse_postorder(self.root)

    def _reverse_postorder(self, node=None):
        if node is None:
            return []

        return (
            self._reverse_postorder(node.right)
            + self._reverse_postorder(node.left)
            + [node.value]
        )
