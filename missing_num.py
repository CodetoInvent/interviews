

def missing_num(nums, n):
    nums = sorted(nums)
    for i in range(n):
        if i == len(nums): return i
        if i < nums[i]:
            return nums[i]-1

def missing_num2(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= nums[i]
        result ^= i

    return result
        
def missing_num3(nums):
    lower = 0
    upper = len(nums) -1

    while lower <= upper:
        middle = (lower + upper) // 2
        value = nums[middle]
        # 0 1 2 3 4
        # 0 1 3 4 5

nums = [0, 2, 3]

# only if nums in 0..n and 0 < nums[i] < n
def missing_num4(nums):
    pass


print missing_num(nums, 5)
print missing_num2(nums)

