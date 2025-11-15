def consecutive_longest(nums):
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            current_num=num
            current_streak=1
            while current_num+1 in num_set:
                current_num+=1
                current_streak+=1
            longest=max(longest,current_streak)
    return longest
print(consecutive_longest([100,4,200,1,3,2]))            