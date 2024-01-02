def count_investable_periods(n, price, max_price, min_price):
    count = 0
    for i in range(n):
        subarray_max = float('-inf')
        subarray_min = float('inf')

        for j in range(i, n):
            subarray_max = max(subarray_max, price[j])
            subarray_min = min(subarray_min, price[j])

            if subarray_max == max_price and subarray_min == min_price:
                count += 1

    return count

# Example usage
n = 4
price = [1, 2, 3, 2]
max_price = 3
min_price = 2

result = count_investable_periods(n, price, max_price, min_price)
print(result)