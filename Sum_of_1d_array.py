def solve(prices):
    n = len(nums)
    rs = [nums[0]]

    for i in range(1, n):
        nums[i] += nums[i-1]
        rs.append(nums)
    return rs

nums = [1, 1, 1, 1, 1]
print(solve(nums))