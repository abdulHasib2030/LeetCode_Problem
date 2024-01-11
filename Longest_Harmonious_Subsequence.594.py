class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        dic = {}
        i, j, n = 0,1, len(nums)
        while j < n:
            if abs(nums[i] - nums[j]) == 1:
                dic[nums[i]] = nums[j]
            i+= 1
            j+= 1
        mx = 0
        for key, value in dic.items():
            cnt = nums.count(key)
            cnt2 = nums.count(value)
            summ = cnt + cnt2
            if mx < summ:
                mx = summ
        return mx


## Efficient Solution
# hash_map = {}
# cur_max = 0
# for num in nums:
#   if num in hash_map:
#       hash_map[num] += 1
#   else:
#       hash_map[num] = 1
# print(hash_map)      
# for key in hash_map:
#     if key-1 in hash_map:
#         cur_max = max(cur_max, hash_map[key] + hash_map[key-1])
#     if key+1 in hash_map:
#         cur_max = max(cur_max, hash_map[key] + hash_map[key+1])

# print(cur_max)


