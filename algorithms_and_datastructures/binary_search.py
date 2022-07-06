import timeit
import random


def binary_search(nums: list[int], target: int):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def default_search(nums: list[int], target: int):
    return next((i for i, v in enumerate(nums) if v == target), -1)


N = 100000000

arr = list(range(N))

binary_search_example_time = timeit.timeit(
    lambda: binary_search(arr, random.randint(0, N)), number=10)
print(f"binary_search avg exec time: {binary_search_example_time}")

default_search_example_time = timeit.timeit(
    lambda: default_search(arr, random.randint(0, N)), number=10)
print(f"default_search avg exec time: {default_search_example_time}")
