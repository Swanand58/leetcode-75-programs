# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

class Solution:
    def longestPalindrome(self, s: str) -> int:

        if len(s) == 1:
            return 1
        
        letter_set = set()
        count = 0

        for letter in s:
            if letter in letter_set:
                letter_set.remove(letter)
                count += 2
            
            else:
                letter_set.add(letter)

        if letter_set:
            count += 1

        return count
