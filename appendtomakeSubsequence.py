# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

# Example 1:

# Input: s = "coaching", t = "coding"
# Output: 4
# Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
# Example 2:

# Input: s = "abcde", t = "a"
# Output: 0

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index, t_index = 0, 0
        s_length, t_length = len(s), len(t)
    
        while s_index < s_length and t_index < t_length:
            if s[s_index] == t[t_index]:
                t_index += 1
            s_index += 1
    
        return t_length - t_index