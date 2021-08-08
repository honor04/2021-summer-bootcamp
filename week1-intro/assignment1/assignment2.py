def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n<= 0:
        return False
    else:
        import math
        end = int(math.sqrt(n) + 1)
        for i in range(2,end):
            if n%i == 0:
                return False
        return True


# DO NOT ALTER BELOW.
assert is_prime(2)
assert not is_prime(15)
assert is_prime(7907)
assert not is_prime(-1)
assert not is_prime(0)

# Q2 Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.
# Input ar = [1,2,3,4,5,6,7], d = 2
# Output [3,4,5,6,7,1,2]

def rotate(ar: [int], d: int) -> [int]:
    d_mod = d%len(ar)
    first_list: list = ar[0:d_mod]
    end_list: list = ar[d_mod:]
    return end_list + first_list


# DO NOT ALTER BELOW.
assert rotate([1,2,3,4,5,6,7], 2) == [3,4,5,6,7,1,2]
assert rotate([1,2,3], 4) == [2,3,1]

# Selection sort - implement a workable selection sort algorithm
# https://www.runoob.com/w3cnote/selection-sort.html 作为参考
# Input students would be a list of [student #, score], sort by score ascending order.

def selection_sort(arr: [[int]]) -> [[int]]:
    if arr == None:
        return arr
    else:
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[j][1] < arr[i][1]:
                    arr[j],arr[i] = arr[i],arr[j]
        return arr


# DO NOT ALTER BELOW.
assert selection_sort([]) == []
assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]


# Q4. Convert a list of Tuples into Dictionary

# tips: copy operation - copy by value, copy by reference

def convert(tup: (any), di: {any, any}) -> None:
    if tup == None:
        di == None
    else:

    pass
    # Do NOT RETURN di, EDIT IN-PLACE


# DO NOT ALTER BELOW.
expected_dict = {}
convert((), expected_dict)
assert expected_dict == {}

convert(('key1', 'val1', 'key2', 'val2'), expected_dict)
assert expected_dict == {'key1': 'val1', 'key2': 'val2'}