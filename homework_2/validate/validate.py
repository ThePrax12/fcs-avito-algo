def solution(pushed, popped):
    pushed_stack = []
    j = 0
    for el in pushed:
        pushed_stack.append(el)
        while pushed_stack != [] and pushed_stack[-1] == popped[j]:
            j += 1
            pushed_stack.pop()
    return pushed_stack == []
