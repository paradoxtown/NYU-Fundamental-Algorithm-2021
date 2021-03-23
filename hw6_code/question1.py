class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


# def remove_outside_range(root, Min, Max):
#     if root is None:
#         return None
#
#     root.left = remove_outside_range(root.left, Min, Max)
#     root.right = remove_outside_range(root.right, Min, Max)
#
#     if root.key < Min:
#         rChild = root.right
#         return rChild
#
#     if root.key > Max:
#         lChild = root.left
#         return lChild
#
#     return root

class Solution1(object):
    def __init__(self):
        self.inorder = []
        self.preorder = []
        self.postorder = []
        self.stack = []

    def build_binary_search_tree(self, root, key):
        if root is None:
            return Node(key)
        if root.key >= key:
            root.left = self.build_binary_search_tree(root.left, key)
        else:
            root.right = self.build_binary_search_tree(root.right, key)
        return root

    def search(self, array, start, end, data):
        for i in range(start, end + 1):
            if array[i] == data:
                return i

    def get_inorder(self, root):
        if root:
            self.get_inorder(root.left)
            self.inorder.append(root.key)
            self.get_inorder(root.right)

    def get_preorder(self, root):
        if root:
            self.preorder.append(root.key)
            self.get_preorder(root.left)
            self.get_preorder(root.right)

    def recover_binary_tree(self, preorder, inorder):
        n = len(preorder)
        if n == 0:
            return None
        node = Node(preorder[0])
        p = self.search(inorder, 0, n - 1, node.key)
        if p - 0 > 0:
            preorder_ = preorder[1:1 + p]
            inorder_ = inorder[:p]
            node.left = self.recover_binary_tree(preorder_, inorder_)
        if n - 1 - p > 0:
            preorder_ = preorder[1 + p:n]
            inorder_ = inorder[p + 1:n]
            node.right = self.recover_binary_tree(preorder_, inorder_)
        return node

    def recover_binary_search_tree(self, preorder):
        n = len(preorder)
        if n == 0:
            return None
        node = Node(preorder[0])
        p = 1
        for i in range(1, n):
            if preorder[i] > node.key:
                break
            p += 1
        if p - 1 > 0:
            node.left = self.recover_binary_search_tree(preorder[1:p])
        if n - p > 0:
            node.right = self.recover_binary_search_tree(preorder[p:n])
        return node

    def recover_expression_tree(self):
        node = Node(self.stack.pop())
        if self.stack:
            top = self.stack.pop()
            if isinstance(top, int):
                node.right = Node(top)
            else:
                self.stack.append(top)
                node.right = self.recover_expression_tree()
        if self.stack:
            top = self.stack.pop()
            if isinstance(top, int):
                node.left = Node(top)
            else:
                self.stack.append(top)
                node.left = self.recover_expression_tree()
        return node


if __name__ == '__main__':
    # build binary tree
    solution = Solution1()
    is_binary_tree = False
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
        root.right = node2
        node1.left = node3
        node1.right = node4
        node2.left = node5
        node2.right = node6
        node3.left = node7

        # verify in order
        solution.inorder = []
        solution.get_inorder(root)
        print(solution.inorder)

        # verify pre order
        solution.preorder = []
        solution.get_preorder(root)
        print(solution.preorder)

        recover_root = solution.recover_binary_tree(solution.preorder, solution.inorder)

        # verify in order
        solution.inorder = []
        solution.get_inorder(recover_root)
        print(solution.inorder)

        # verify pre order
        solution.preorder = []
        solution.get_preorder(recover_root)
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

        solution.preorder = []
        solution.get_preorder(root)
        print(solution.preorder)

        recover_root = solution.recover_binary_search_tree(solution.preorder)

        # verify in order
        solution.inorder = []
        solution.get_inorder(recover_root)
        print(solution.inorder)

        # verify pre order
        solution.preorder = []
        solution.get_preorder(recover_root)
        print(solution.preorder)
    else:
        solution.stack = [8, 4, '/', 5, 6, 2, '-', '*', '+']
        recover_root = solution.recover_expression_tree()

        # verify in order
        solution.inorder = []
        solution.get_inorder(recover_root)
        print(solution.inorder)

        # verify pre order
        solution.preorder = []
        solution.get_preorder(recover_root)
        print(solution.preorder)

