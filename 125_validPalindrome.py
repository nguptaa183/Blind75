# Leetcode 125 Valid Palindrome

def isPalindrome(self, s: str) -> bool:
    sout = ""
    for i in s:
        if not i.isalpha() and not i.isdigit():
            continue
        sout += i
    sout = sout.lower()
    if sout == sout[::-1]:
        return True
    return False

# Using two pointers without the extra space/memory


def isPalindrome(self, s: str) -> bool:
    l,r=0, len(s)-1

    while l<r:
        while l<r and not isAplhaNumeric(s[l]):
            l=l+1
        while l<r and not isAplhaNumeric(s[r]):
            r=r-1
        if s[l].lower() != s[r].lower():
            return False
        l,r=l+1,r-1
    return True


def isAplhaNumeric(c):
    return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"))
