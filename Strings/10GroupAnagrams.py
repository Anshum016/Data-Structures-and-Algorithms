import collections  # Correct the module name

def groupAnagrams(strs):
    d = collections.defaultdict(list)  # Use 'collections', not 'collection'
    
    for s in strs:
        count = [0] * 26  # Create a list to store letter frequencies
        
        for letter in s:
            count[ord(letter) - ord('a')] += 1  # Update frequency count for each letter
        
        d[tuple(count)].append(s)  # Append the word to the correct group, based on its count
    
    return d.values()

# Input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print('Our Answer:', groupAnagrams(strs))
