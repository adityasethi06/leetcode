
def two_sum(lst, target):
    map = {}

    for ind, n in enumerate(lst):
        if (target - n) in map:
            return [map[target-n], ind]
        map[n] = ind
    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 7, 11, 15, 6], 30))

# TC: O(n)
