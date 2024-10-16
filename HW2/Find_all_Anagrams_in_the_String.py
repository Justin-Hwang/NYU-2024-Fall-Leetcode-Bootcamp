from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Base case: if the length of p is greater than s, no anagram is possible
        if len(p) > len(s):
            return []
        
        # Initialize the result list
        result = []
        
        # Frequency count of characters in p
        p_count = Counter(p)
        
        # Frequency count of the current window in s
        s_count = Counter()
        
        # Window size is the length of p
        window_size = len(p)
        
        # Iterate through the string s with the sliding window
        for i in range(len(s)):
            # Add the current character to the window
            s_count[s[i]] += 1
            
            # Once the window is the size of p, check for anagrams
            if i >= window_size:
                # Remove the character that is out of the window
                left_char = s[i - window_size]
                if s_count[left_char] == 1:
                    del s_count[left_char]
                else:
                    s_count[left_char] -= 1
            
            # Compare the two frequency counters
            if s_count == p_count:
                # If they are equal, add the starting index to the result
                result.append(i - window_size + 1)
        
        return result

        