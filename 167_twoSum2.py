def twoSumII(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        if (nums[l]+nums[r]) == target:
            return [l+1, r+1]
        elif (nums[l]+nums[r]) > target:
            r = r-1
        else:
            l = l+1


nums = [2, 7, 11, 15]
target = 9
print(twoSumII(nums, target))
