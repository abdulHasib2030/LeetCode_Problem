nums = [0,0,0,0,0]
goal = 0

def helper(nums, goal):
  summ, count = 0,0
  i, j, n = 0,0,len(nums)
  while j < n:
    summ += nums[j]
    while i <= j and summ > goal:
      summ -= nums[i]
      i+=1
    count += j-i + 1
    j+=1
  return count

print(helper(nums, goal) - helper(nums, goal - 1))