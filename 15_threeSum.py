def threeSum(numbers):
    i,j = 0, len(numbers)-1
    while i<j:
        m = (i+j)//2
        if numbers[m] == target:
            return [i+1, j+1]
        elif numbers[m] < target:
            i=m+1
        else:
            j=m-1
    print(i,j)

numbers = [2,7,11,15]
target=9
print(threeSum(numbers))

