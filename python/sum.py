def two_sum(nums,target):
    num_map={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in num_map:
            return num_map[complement],i
        num_map[num]=i
    return None   
print(two_sum([2,15,11,7],9))    