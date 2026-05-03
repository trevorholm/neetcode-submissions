class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Space: O(m) extra space & O(m * n) space for the output list
        # Time: O(m * n)
        
        res = defaultdict(list) # mapping charCount to list of Anagrams, default hash map where the default value is a list so we don't have to deal with one edge case

        for s in strs:
            count = [0] * 26 # letters a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1 # Map each letter to a specific index, taking the ASCII value to compare 
            res[tuple(count)].append(s) # Append all anagrams with this count together, lists cannot be keys so we change the count to a tuple (Python exclusive)

        return list(res.values()) # Return the list of values, the anagrams grouped together