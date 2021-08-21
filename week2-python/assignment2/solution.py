# Q5. Find left-most and right-most index for a target in a sorted array with duplicated items.
# provided an example of slow version of bsearch_slow with O(n) time complecity.
# your solution should be faster than bsearch_slow


def bsearch_slow(arr: [int], target: int) -> (int, int):
    start = -1
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            if start == -1:
                start = i
            count += 1
    return start, start + count - 1


def create_arr(count: int, dup: int) -> [int]:
    return [-1, -1, -1] + [dup for i in range(count)] + [100, 100, 100]


# Complete this
def bsearch(arr: [int], t: int) -> (int, int):
    return find_left(arr, t), find_right(arr, t)


def find_left(arr: [int], t: int):
    start = 0
    end = len(arr) - 1
    while start < end - 1:
        mid = (start + end) // 2
        if arr[mid] >= t:
            end = mid
        else:
            start = mid + 1

    if arr[start] == t:
        return start
    if arr[end] == t:
        return end
    return -1


def find_right(arr: [int], t: int):
    start = 0
    end = len(arr) - 1
    while start < end - 1:
        mid = (start + end) // 2
        if arr[mid] > t:
            end = mid - 1
        else:
            start = mid

    if arr[end] == t:
        return end
    if arr[start] == t:
        return start
    return -1


print(bsearch_slow(create_arr(10000, 5), 5))
assert bsearch_slow(create_arr(10000, 5), 5) == (3, 10002)
print(bsearch(create_arr(1000, 5), 5))
# assert bsearch(create_arr(1000, 5), 5) == (0, 999)

import timeit

# slow version rnning 100 times = ? seconds
# n 10000, logn 10 - 20 = 1000 / 2 ~= 500 = 30
# temp = create_arr(10000, 5)
# print(timeit.timeit(lambda: bsearch_slow(temp, 5), number=1000))
# print(timeit.timeit(lambda: bsearch(temp, 5), number=1000))
# print(timeit.timeit(lambda: bsearch(create_arr(10000, 5), 5), number=1000))
# # add your version and compare if faster.


def bsearch2(arr: [int], target: int) -> (int):
    result = []
    # 找下限
    left = 0
    RIGHT = len(arr) - 1
    right = RIGHT
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        if arr[mid] < target:
            left = mid + 1
    if target != arr[left]:
        return [-1, -1]
    result.append(left)
    if left == RIGHT:
        return (RIGHT, RIGHT)

    print(left)
    # 找上限
    left = 0
    RIGHT = len(arr) - 1
    right = RIGHT

    while left < right - 1:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid
        if arr[mid] > target:
            right = mid - 1

    result.append(right)
    return result


print(bsearch2(create_arr(1000, 5), 5))
