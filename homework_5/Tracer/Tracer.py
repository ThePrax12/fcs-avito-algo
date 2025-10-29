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


# @trace
# def power(base, exp=2):
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     return base * power(base, exp - 1)
#
# power(2, 4)


# -> power(2, 4)
#   -> power(2, 3)
#     -> power(2, 2)
#       -> power(2, 1)
#       <- power(2, 1) = 2
#     <- power(2, 2) = 4
#   <- power(2, 3) = 8
# <- power(2, 4) = 16
