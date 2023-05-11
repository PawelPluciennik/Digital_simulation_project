from Tree.TreeNode import TreeNode


class Tree:
    def __init__(self):
        self.root = None

    def _insert_node(self, current_node, new_node):
        if current_node is None:
            self.root = new_node
        elif new_node.data.id < current_node.data.id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_node(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_node(current_node.right, new_node)

    def add(self, data):
        new_node = TreeNode(data)
        self._insert_node(self.root, new_node)

    def _find_node(self, current_node, id):
        if current_node is None:
            return None
        elif id == current_node.data.id:
            return current_node.data
        elif id < current_node.data.id:
            return self._find_node(current_node.left, id)
        else:
            return self._find_node(current_node.right, id)

    def find(self, id):
        return self._find_node(self.root, id)

    def _delete_node(self, current_node, id):
        if current_node is None:
            return current_node
        elif id < current_node.data.id:
            current_node.left = self._delete_node(current_node.left, id)
        elif id > current_node.data.id:
            current_node.right = self._delete_node(current_node.right, id)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            temp = self._find_min_node(current_node.right)
            current_node.data = temp.data
            current_node.right = self._delete_node(current_node.right, temp.data.id)
        return current_node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, id):
        self.root = self._delete_node(self.root, id)

    def _print_node(self, node):
        if node is not None:
            self._print_node(node.left)
            print(node.data.id) #node.data.name
            self._print_node(node.right)

    def print_tree(self):
        self._print_node(self.root)
