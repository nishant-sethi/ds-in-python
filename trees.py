class Tree:
    def add_to_tree(self):
        pass

    def delete_from_tree(self):
        pass

    def print_tree(self):
        pass


class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(Tree):
    def add_to_tree(self):
        pass

    def delete_from_tree(self):
        pass

    def print_preorder(self, root: BinaryTreeNode):
        if root is not None:
            print(root.data, end=' ')
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_inorder(self, root: BinaryTreeNode):
        if root is not None:
            self.print_inorder(root.left)
            print(root.data, end=' ')
            self.print_inorder(root.right)

    def print_postorder(self, root: BinaryTreeNode):
        if root is not None:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root.data, end=' ')

    def print_levelorder(self, root: BinaryTreeNode):
        pass


class BinarySearchTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()
        self.root = None

    def add_node_to_tree(self, data, root: BinaryTreeNode):
        if not self.search_node_from_tree(root, data):
            if root is None:
                self.root = BinaryTreeNode(data)
                return
            if data > root.data:
                if root.right is None:
                    root.right = BinaryTreeNode(data)
                    return
                else:
                    self.add_node_to_tree(data, root.right)
            else:
                if root.left is None:
                    root.left = BinaryTreeNode(data)
                    return
                else:
                    self.add_node_to_tree(data, root.left)
        else:
            print('Element Already exists in the tree')

    def delete_node_from_tree(self):
        pass

    def search_node_from_tree(self, root: BinaryTreeNode, data):
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search_node_from_tree(root.right, data)
        elif root.data > data:
            return self.search_node_from_tree(root.left, data)

    def is_bst(self, root: BinaryTreeNode):
        if root.left is None and root.right is None:
            return True
        else:
            return root.left.data < root.data and root.right.data > root.data and self.is_bst(root.left) and self.is_bst(root.right)

    def print_tree(self, root):
        print('Inorder Traversal')
        super().print_inorder(root)
        print('\n')

        print('Preorder Traversal')
        super().print_preorder(root)
        print('\n')

        print('Post Order Traversal')
        super().print_postorder(root)
        print('\n')


class NaryTree(Tree):
    def add_to_tree(self):
        pass

    def delete_from_tree(self):
        pass

    def print_tree(self):
        pass


class Trie(NaryTree):
    pass


class DecisionTree(Tree):
    pass


tree = BinarySearchTree()
tree.add_node_to_tree(10, tree.root)
tree.add_node_to_tree(7, tree.root)
tree.add_node_to_tree(13, tree.root)
tree.add_node_to_tree(5, tree.root)
tree.add_node_to_tree(9, tree.root)
tree.add_node_to_tree(9, tree.root)
tree.add_node_to_tree(11, tree.root)
tree.add_node_to_tree(19, tree.root)
tree.add_node_to_tree(1, tree.root)
tree.add_node_to_tree(6, tree.root)
tree.print_tree(tree.root)

# print("Enter the element you want to search for")
# element_to_find = int(input())
# node = tree.search_node_from_tree(tree.root,element_to_find)
# if not node:
#     print('element does not exist in the tree')
# else:
#     print('Element found', node.data)

print(tree.is_bst(tree.root))
