import random
import time

from Makeheap import makeheap_n_log_n, makeheap


def benchmark(n, repeats=5):
    print(f"n = {n}")
    rng = random.Random(42)
    data = [rng.randint(-(10**9), 10**9) for _ in range(n)]

    t_total = 0.0
    for _ in range(repeats):
        arr = data.copy()
        t0 = time.perf_counter()
        makeheap_n_log_n(arr)
        t1 = time.perf_counter()
        t_total += t1 - t0
    print(f"makeheap_n_log_n: {t_total} s")

    t_total = 0.0
    for _ in range(repeats):
        arr = data.copy()
        t0 = time.perf_counter()
        makeheap(arr)
        t1 = time.perf_counter()
        t_total += t1 - t0
    print(f"makeheap: {t_total} s")


for n in [10**3, 10**4, 10**5, 5 * 10**6]:
    benchmark(n)


# n = 1000
# makeheap_n_log_n: 0.001975458999999999 s
# makeheap       : 0.0020172499999999913 s
# n = 10000
# makeheap_n_log_n: 0.022497750000000004 s
# makeheap       : 0.021535 s
# n = 100000
# makeheap_n_log_n: 0.222395875 s
# makeheap       : 0.26267195900000007 s
# n = 5000000
# makeheap_n_log_n: 16.179951624999998 s
# makeheap       : 11.706338916999997 s
