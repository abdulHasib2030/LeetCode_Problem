nums = [23,2,6,4,7]
k = 13
n = len(nums)
flag = True
temp = nums[0]
for i in range(1,n):
  temp += nums[i]
  if k == temp:
    flag = False
    break
  temp -= nums[i-1]
if flag == False:
  print(True)
elif sum(nums) % k == 0:
  print(True)
else:
  print(False)


