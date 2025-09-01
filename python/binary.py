def locate_cards(cards,query):
    low,high=0,len(cards)-1
    while low<=high:
        mid=(low+high)//2
        if cards[mid]==query:
            return mid
        elif cards[mid]<query:
            low=mid+1
        else:
            high=mid-1
    return -1
result=locate_cards([1,2,3,4,5],2)   
print(result) 
