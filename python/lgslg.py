def lgs(arr):
    if len(arr) < 2:
        return None
    max1,max2=float('-inf'),float('-inf')
    for x in arr:
        if x>max1:
            max2=max1
            max1=x
        elif x>max2 and x!=max1:
            max2=x
    return max1,max2        
arr=input("enter the numbers seperated by space").split()
nums=list(map(int,arr))
print("the largest and second largest  is",lgs(nums))               