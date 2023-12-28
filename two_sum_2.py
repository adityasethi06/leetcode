# find indices of 2 nums that add upto a target
# return indices should be one based and not 0 based
# also given list is sorted

# assumption:
# there always exists one solution

def two_sum(lst, target):
    l, r = 0, len(lst)-1

    while l < r:
        current_sum = lst[l] + lst[r]
        if current_sum < target:
            l += 1
        elif current_sum > target:
            r -= 1
        else:
            return [l+1, r+1]

print(two_sum([1,3,5,7,9], 14)) 