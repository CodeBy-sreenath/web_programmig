def prod(nums):
    n=len(nums)
    answer=[1]*n
    prefix=1
    for i in range(n-1,-1,-1):
        answer[i]=prefix
        prefix=prefix*nums[i]
    suffix=1    
    for i in range(n):
        answer[i]=answer[i]*suffix
        suffix=suffix*nums[i]    
    return answer
nums=[1,2,3,4]
print(prod(nums))    