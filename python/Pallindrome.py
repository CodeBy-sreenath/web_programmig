n=int(input("enter a number"))
temp=n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse is",rev)
if temp==rev:
    print("pallindrome")
else:
    print("not a pallindrome")      
    