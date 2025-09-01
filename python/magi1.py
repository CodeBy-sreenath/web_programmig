N=int(input("enter the orde"))
if N<1:
    print("value error")
elif N==2:
     print("No magic squre with order 2")
else:
     magic = [[0 for _ in range(N)] for _ in range(N)]
     i=0 
     j=N // 2
     for num in range(1,N*N+1):
         magic[i][j]=num 
         new_i=(i-1)%N
         new_j=(i+1)%N 
         if magic[new_i][new_j] !=0:
             i=(i+1)%N
         else:
             i=new_i
             j=new_j
     print(magic)        
            
            