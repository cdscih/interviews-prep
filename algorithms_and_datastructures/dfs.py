
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


r_dfs_res = []


def r_dfs(root: Node = None):
    if root is None:
        return
    r_dfs_res.append(root.val)
    if root.left:
        r_dfs(root.left)
    if root.right:
        r_dfs(root.right)


def i_dfs(root: Node):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def preorder_dfs(root: Node):
    tpl = ""
    
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        tpl += str(node.val) + " "
        stack.append(node.right)
        stack.append(node.left)
    
    return tpl


tree = Node(5)
tree.left = Node(15)
tree.right = Node(1)
tree.left.left = Node(2)
tree.left.right = Node(22)
tree.right.left = Node(6)
tree.right.right = Node(32)
tree.left.left.left = Node(183)


r_dfs(tree)
print(r_dfs_res)
print(i_dfs(tree))
print(preorder_dfs(tree))
