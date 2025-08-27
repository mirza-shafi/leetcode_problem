nums = [1,2,3,4,5,1]
nums.sort()
flag = True
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        flag = True
        break
    else:
        flag = False
print(flag)