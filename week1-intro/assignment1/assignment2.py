# Q2 Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.
# Input ar = [1,2,3,4,5,6,7], d = 2
# Output [3,4,5,6,7,1,2]

def rotate(ar: [int], d: int) -> [int]:
    d_mod: int = d % len(ar)
    first_list: list = ar[0:d_mod]
    end_list: list = ar[d_mod:]
    return end_list + first_list


# DO NOT ALTER BELOW.
assert rotate([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]
assert rotate([1, 2, 3], 4) == [2, 3, 1]


def rotation(arr: [int]) -> [int]:
    for i in range(len(arr) // 2):
        Inter_1 = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = Inter_1


def rotate(ar: [int], d: int) -> [int]:
    d_mod: int = d % len(ar)
    rotation(ar[0:d_mod])
    rotation(ar[d_mod:])
    return rotation(ar)


assert rotate([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]
assert rotate([1, 2, 3], 4) == [2, 3, 1]
