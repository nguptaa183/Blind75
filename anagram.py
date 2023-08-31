# Leetcode 242 Valid Anagram

def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    d1,d2={},{}
    for i in s:
        d1[i]=d1.get(i,0)+1
    for j in t:
        d2[j]=d2.get(j,0)+1
    if d1==d2:
        return True
    return False