import heapq
import random


def max_h(nums: list[int]):
    inverse = [-n for n in nums]
    heapq.heapify(inverse)
    return -(heapq.heappop(inverse))


def min_h(nums: list[int]):
    heapq.heapify(nums)
    return heapq.heappop(nums)


arr = [random.randint(0, 100) for _ in range(15)]

print(max_h(arr))
print(min_h(arr))
