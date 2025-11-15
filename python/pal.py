def palindrome(s):
    str=""
    for i in s:
        str=i+str
    if s==str:
        print("palindrome")
    else:
        print("not pallindrome")
s=input("enter the string")
palindrome(s)                