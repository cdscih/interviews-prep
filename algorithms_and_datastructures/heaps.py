import heapq
import random


def create_max_h(nums: list[int]):
    inverse = [-n for n in nums]
    heapq.heapify(inverse)
    return inverse

def create_min_h(nums: list[int]):
    heapq.heapify(nums)
    return nums


arr = [random.randint(0, 100) for _ in range(15)]

max_heap = create_max_h(nums)
print(max_heap)

min_heap = create_min_h(nums)
print(min_heap)

print("Max in max_heap: " + -(heapq.heappop(inverse)))
print("Min in min_heap: " + heapq.heappop(nums))
