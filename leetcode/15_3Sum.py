# 15. 3Sum medium
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Runtime: 816 ms, faster than 77.66% of Python3 online submissions for 3Sum.
        Memory Usage: 16.8 MB, less than 20.61% of Python3 online submissions for 3Sum.
        '''
        if len(nums) < 3: return []
        target = 0
        start = 0

        results = []
        # Sort the array
        nums.sort()

        # While 2 less than array (triple pointer)
        while start < len(nums) - 2:
            # Smallest value is larger than target, break
            if nums[start] > target: break

            # If start index is over 0 and curr value == previous value
            # we have a duplicate, skip to next index
            if start > 0 and nums[start] == nums[start-1]:
                start += 1
                continue

            # Index will bound between start and end
            # Initialize to start + 1
            index = start + 1
            end = len(nums) - 1
            print(index, start, end)
            while(index < end):

                my_sum = nums[start] + nums[index] + nums[end]

                if my_sum == target:
                    results.append([nums[start],nums[index],nums[end]])

                    # While duplicates, skip them
                    while(index < len(nums) - 1 and nums[index] == nums[index+1]):
                      index += 1

                    # While duplicates, skip them
                    while(end < len(nums) - 1 and nums[end] == nums[end-1]):
                      end -= 1

                    index +=1
                    end -= 1

                elif my_sum < target:
                  index += 1

                elif my_sum > target:
                  end -= 1
            start += 1

        return results
