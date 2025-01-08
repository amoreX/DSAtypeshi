def solve(nums, target):
  d={}
  for i in range(len(nums)):
    if (target-nums[i]) in d:
      return [i,d[target-nums[i]]] if i< d[target-nums[i]] else [d[target-nums[i]],i]
    d[nums[i]]=i
nums=[2,7,11,15]
tar=9
p=solve(nums,tar)
print(p)