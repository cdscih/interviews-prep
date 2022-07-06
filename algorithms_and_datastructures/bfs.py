
import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


r_dfs_res = []


def i_bfs(root: Node):
    res = []
    q = collections.deque([root])
    while q:
        for _ in range(len(q)):
            node = q.pop()
            res.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
    return res


tree = Node(5)
tree.left = Node(15)
tree.right = Node(1)
tree.left.left = Node(2)
tree.left.right = Node(22)
tree.right.left = Node(6)
tree.right.right = Node(32)
tree.left.left.left = Node(183)


print(i_bfs(tree))
