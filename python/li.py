def lin(arr,key):
    for i, v in enumerate(arr):
        if v==key:
            print("the value is found at index",i)
    return -1
arr=input("enter the numbers seperated by space").split()
num=list(map(int,arr))
key=int(input("enter the value to found"))
lin(num,key)    
    
        