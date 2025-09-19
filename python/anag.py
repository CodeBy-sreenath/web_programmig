from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
            print(count)

        key = tuple(count)
        
        anagram_map[key].append(word)

    # Convert dictionary values to list of lists
    grouped = list(anagram_map.values())

    # Display result in terminal
    print("\nGrouped Anagrams:")
    for i, group in enumerate(grouped, start=1):
        print(f"Group {i}: {group}")

    return grouped


# ---------- Main program ----------
# Take input from the user
user_input = input("Enter words separated by spaces: ")

# Convert string into list
words = user_input.split()

# Call function
groupAnagrams(words)
