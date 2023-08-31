# Leetcode 217 Contains Duplicate

def containsDuplicate(self, nums: List[int]) -> bool:
    s=set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False