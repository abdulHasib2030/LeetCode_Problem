class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst = set()
        nums.sort()
        ans = []
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            k = j+1
            l = len(nums) -1
            while k < l:
              sum = nums[i] + nums[j] + nums[k] + nums[l]
              if sum == target:
                lst.add((nums[i], nums[j], nums[k], nums[l]))
                k += 1
                l -= 1
              elif sum < target:
                k += 1
              else:
                l-=1
            
        ans = list(lst)
        return (ans)
        
        
        