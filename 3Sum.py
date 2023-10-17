class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        ansSet = set()
        lst = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                suma = nums[i] + nums[j] + nums[k]
                if suma == target:
                    ansSet.add((nums[i], nums[j], nums[k]))
                    j +=1
                    k -=1
                elif suma < target:
                  j +=1
                else:
                  k -= 1
        lst = list(ansSet)

        return (lst)