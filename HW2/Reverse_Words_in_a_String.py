class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by spaces into a list of words
        # Use `split()` without any arguments to handle multiple spaces, it will automatically ignore extra spaces
        words = s.split()
        
        # Step 2: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 3: Join the reversed list of words with a single space
        result = ' '.join(reversed_words)
        
        return result