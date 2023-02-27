def shift_list(nums, n):
    # Определяем индекс, с которого начнется новый список
    idx = n % len(nums)
    # Склеиваем два среза
    return nums[idx:] + nums[:idx]

nums = [1, 2, 3, 4, 5, 6, 7]
n = 8
shifted_nums = shift_list(nums, n)
print(shifted_nums) # [5, 6, 7, 1, 2, 3, 4]

print(n % len(nums))
print(n // len(nums))
