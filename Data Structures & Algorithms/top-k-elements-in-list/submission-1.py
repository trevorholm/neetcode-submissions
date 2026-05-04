class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Space: O(n) Time: O(n)
        
        count = {} # Hash map to count the occurences of the values
        freq = [[] for i in range(len(nums) + 1)] #

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Count how many times an element occurs, if n doesn't exist in our hashmap we put a default value of 0
        for n, c in count.items(): # Going through each value we counted
            freq[c].append(n) # n occurs c times

        res = [] # Top k elements
        for i in range(len(freq) - 1, 0, -1): # Last index, go all the way up until 0, decrement by 1
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res # Guaranteed to reach this if statement at some point, so no need to put return statement outside of the if statement