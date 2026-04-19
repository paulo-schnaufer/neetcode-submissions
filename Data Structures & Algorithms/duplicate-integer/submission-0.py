class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compar = []
        for num in nums:
            if num in compar:
                return True
            else:
                compar.append(num)
        return False