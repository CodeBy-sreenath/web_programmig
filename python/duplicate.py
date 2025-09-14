def hash_duplicate(lst):
    seen=set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False    
print(hash_duplicate([1,2,3,4,5,6]))
print(hash_duplicate([1,2,3,4,5,1]))
       