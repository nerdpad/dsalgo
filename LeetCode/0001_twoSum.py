class Solution:
	"""
	https://leetcode.com/problems/two-sum/
	"""
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		'''
		# brute force - time: O(n^2), space: O(1)
		for i in range(len(nums) - 1):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]
		'''

		visited_elements = {}
		for index, num in enumerate(nums):
			complement = target - num
			if complement in visited_elements:
				return [index, visited_elements[complement]]
			
			visited_elements[num] = index

if __name__ == '__main__':
	s = Solution()
	result = s.twoSum([2,4,5,6,7], 9)
	print(result)