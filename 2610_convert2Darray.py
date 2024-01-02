from collections import Counter


def res(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)

    result = list((counter_a - counter_b).elements())

    return result


def twoSumII(nums):
    r = []
    while len(nums) != 0:
        m = []
        for i in nums:
            if i not in m:
                m.append(i)
        r.append(m)
        nums = res(nums, m)
    return r


def twoSumII_Optimal(nums):

    countDict = {}
    ans = []

    for i in nums:
        if i not in countDict:
            countDict[i] = 0

        item = countDict[i]

        if item == len(ans):
            ans.append([])

        ans[item].append(i)

        countDict[i] += 1

    return ans


nums = [1, 3, 4, 1, 2, 3, 1]
print(twoSumII(nums))
print(twoSumII_Optimal(nums))
