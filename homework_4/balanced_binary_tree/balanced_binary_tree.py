def height(node):
    if node is None:
        return 0

    h1 = height(node.left)
    if h1 == -1:
        return -1
    h2 = height(node.right)
    if h2 == -1:
        return -1

    if abs(h1 - h2) > 1:
        return -1

    return max(h1, h2) + 1


def is_balanced(node):

    return height(node) != -1
