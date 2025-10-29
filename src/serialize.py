class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # TODO: preorder with '#' for None, space-separated
    # preorder traversal: node, left, right
    vals = []

    def helper(node):
        if node is None:
            vals.append('#')
            return
        vals.append(str(node.val))
        helper(node.left)
        helper(node.right)

    helper(root)
    return ' '.join(vals)

def deserialize(s):
    # TODO: rebuild from tokens
    if not s:
        return None

    tokens = iter(s.split())

    def helper():
        try:
            tok = next(tokens)
        except StopIteration:
            return None
        if tok == '#':
            return None
        # try to convert to int when possible, otherwise keep string
        try:
            val = int(tok)
        except ValueError:
            val = tok
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node

    return helper()
