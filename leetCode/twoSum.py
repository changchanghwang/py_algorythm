nums = [3,2,4]
target = 6

def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                  
print(twoSum(nums,target))