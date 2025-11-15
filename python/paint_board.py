def min_time_paint(boards,k):
    low=max(boards)
    high=sum(boards)
    result=high
    while(low<=high):
        mid=(low+high)//2
        if is_possible(boards,k,mid):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result        
def is_possible(boards,k,max_value):
    painter_count=1
    time_count=0
    for length in boards:
        if time_count+length<=max_value:
            time_count+=length
        else:
            painter_count+=1
            time_count=length 
        if painter_count>k:
            return False
    return True 
boards=[10,20,30,40]
k=2
print("the minimum time is",min_time_paint(boards,k))                         