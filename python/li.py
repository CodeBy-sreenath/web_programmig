#given a list that is obtained by rotrating a soreted list an unknown number of time we need to find the number(minimum)
def cound_rotations(nums):
    position=0
    while position<len(nums):
        if position>0 and nums[position]<nums[position-1]:
            return position
        position+=1
    return 0
print(cound_rotations([15,18,6,3,2,12]))    