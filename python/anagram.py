from collections import Counter
def anagram(S,T):
    return Counter(S)==Counter(T)
print(anagram("listen","silent"))
print(anagram("helo","billion"))