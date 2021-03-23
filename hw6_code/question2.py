from question1 import Node, Solution1


class Solution2(Solution1):
    def __init__(self):
        super().__init__()

    def prune_single(self, node):
        if node is None:
            return None
        node.left = self.prune_single(node.left)
        node.right = self.prune_single(node.right)
        if node.left is not None and node.right is None:
            return node.left
        if node.left is None and node.right is not None:
           return node.right
        return node

    def prune_range(self, node, start, end):
        if node is None:
            return None
        node.left = self.prune_range(node.left, start, end)
        node.right = self.prune_range(node.right, start, end)
        if node.key < start:
            return node.right
        if node.key > end:
            return node.left
        return node


if __name__ == '__main__':
    solution = Solution2()
    is_binary_tree = True
    is_binary_search_tree = False
    if is_binary_tree:
        root = Node(10)
        node1 = Node(11)
        node2 = Node(2)
        node3 = Node(5)
        node4 = Node(8)
        node5 = Node(17)
        node6 = Node(13)
        node7 = Node(23)
        root.left = node1
        node1.left = node3
        node3.left = node7

        solution.inorder = []
        solution.get_inorder(root)
        print(solution.inorder)

        solution.preorder = []
        solution.get_preorder(root)
        print(solution.preorder)

        prune_root = solution.prune_single(root)

        solution.inorder = []
        solution.get_inorder(prune_root)
        print(solution.inorder)

        solution.preorder = []
        solution.get_preorder(prune_root)
        print(solution.preorder)
    elif is_binary_search_tree:
        root = None
        root = solution.build_binary_search_tree(root, 10)
        root = solution.build_binary_search_tree(root, 11)
        root = solution.build_binary_search_tree(root, 2)
        root = solution.build_binary_search_tree(root, 5)
        root = solution.build_binary_search_tree(root, 8)
        root = solution.build_binary_search_tree(root, 17)
        root = solution.build_binary_search_tree(root, 13)
        root = solution.build_binary_search_tree(root, 23)

        solution.inorder = []
        solution.get_inorder(root)
        print(solution.inorder)

        solution.preorder = []
        solution.get_preorder(root)
        print(solution.preorder)

        prune_root = solution.prune_range(root, 7, 14)

        solution.inorder = []
        solution.get_inorder(prune_root)
        print(solution.inorder)

        solution.preorder = []
        solution.get_preorder(prune_root)
        print(solution.preorder)