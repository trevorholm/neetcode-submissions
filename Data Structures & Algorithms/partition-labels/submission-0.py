class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Space: O(m) Time: O(n)
        lastIndex = {} # Create a hashmap, maps every char to last index

        for i, c in enumerate(s):
            lastIndex[c] = i # Take the char and set its lastIndex to i
        
        res = []
        size = end = 0 # Size of the partition, and end of partition
        for i, c in enumerate(s):
            size += 1 # Increment size
            end = max(end, lastIndex[c]) # Assign end to check if current end or the lastIndex is a greater index

            if i == end:
                res.append(size) # Add the size to the result
                size = 0 # Reset size for the next partition
        return res