def lin(arr,v):
    for i, val in enumerate(arr):
        if val == v:
            return i
    return -1