from collections import Counter
def freq_counter(nums,k):
    freq=Counter(nums)
    sorted_num=sorted(freq.keys(),key=lambda X:freq[X],reverse=True)
    return sorted_num[:k]
nums=input("enter the number seperated by space").split()
num=list(map(int,nums))
k=int(input("enter the frequency"))
print("Most frequent numbers:", freq_counter(num, k))