def minInList(nums):
  minValue = nums[0]
  for i in nums:
    if i < minValue:
      minValue = i
  return minValue

print(minInList([6, 89, 0, -6, 65, 1]))