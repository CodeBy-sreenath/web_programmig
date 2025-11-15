def pali(s):
    string=""
    for i in s:
        string=string+i
    if s==string:
        print("palindrome")
    else:
        print("the string is not palindrome")
s=input("enter the string")
pali(s)               