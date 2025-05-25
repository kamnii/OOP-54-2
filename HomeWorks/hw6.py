def two_sum(nums, num):
    lst = []
    for i in nums:
        for j in nums:
            if i + j == num:
                lst.append(nums.index(i))
    return lst


lst = [2, 7, 11, 15]
target = 9

print(two_sum(lst, target))
