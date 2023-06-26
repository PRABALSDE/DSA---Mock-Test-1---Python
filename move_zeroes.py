def moveZeroes(nums):
    left = right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

nums = [0, 1, 5, 0, 9]
moveZeroes(nums)
print(nums) # Add solution for moving zeros to the end of an array
# Output: [1, 5, 9, 0, 0]
