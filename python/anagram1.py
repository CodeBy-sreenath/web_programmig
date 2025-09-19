from collections import defaultdict
def groupanagrams(str):
    annagram_map=defaultdict(list)
    for word in str:
        count=[0]*26
        for c in word:
            count[ord(c)-ord('a')]+=1
        key=tuple(count) 
        annagram_map[key].append(word)
    grouped=list(annagram_map.values())
    print("Grouped anagram is")
    for i,group in enumerate(grouped,start=1):
        print(f"Group {i}:{group}")
    return grouped
userinput=input("enter words seperated by space")
words=userinput.split()
groupanagrams(words)
         
            
        
        
    