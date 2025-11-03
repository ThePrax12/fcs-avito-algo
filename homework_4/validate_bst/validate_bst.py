def validate(node, min_val=float("-inf"), max_val=float("inf")):
    if node is None:
        return True

    if node.value >= max_val or node.value <= min_val:
        return False

    return validate(node.left, min_val, node.value) and validate(
        node.right, node.value, max_val
    )
