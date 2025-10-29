def trace(func):
    depth = 0

    def wrapper(*args, **kwargs):
        nonlocal depth

        all_args = [str(arg) for arg in args]
        all_args.extend([f"{k}={v}" for k, v in kwargs.items()])
        args_str = ", ".join(all_args)

        print("  " * depth + f"-> {func.__name__}({args_str})")
        depth += 1

        result = func(*args, **kwargs)

        depth -= 1
        print("  " * depth + f"<- {func.__name__}({args_str}) = {result}")

        return result

    return wrapper


@trace
def permutations(nums):

    if len(nums) <= 1:
        return [nums]

    result = []

    for i in range(len(nums)):
        current = nums[i]

        remaining = nums[:i] + nums[i + 1 :]

        for perm in permutations(remaining):
            result.append([current] + perm)

    return result
