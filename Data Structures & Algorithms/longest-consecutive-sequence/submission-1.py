from typing import List


class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
      return 0

    nums.sort()
    longest = 1
    count = 1
    x = nums[0]  # Start with the first number

    for i in range(1, len(nums)):
      y = x + 1

      if nums[i] == y:
        count += 1
        x = y  # Advance x to the next number in the streak
      elif nums[i] == x:
        continue  # Ignore duplicates
      else:
        # Streak broke: start a new streak from the current number
        x = nums[i]
        count = 1

      longest = max(longest, count)

    return longest