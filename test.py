nums=[5,7,7,8,8,10]
target=8
ind=[nums.index(target),len(nums)-nums[::-1].index(target)-1]
print(ind)