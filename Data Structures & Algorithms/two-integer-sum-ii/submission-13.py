class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in idx:
                return [1+idx[diff], 1 +i]

            idx[num] = i