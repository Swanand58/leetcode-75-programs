# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

# Example 1:

# Input: title = "capiTalIze tHe titLe"
# Output: "Capitalize The Title"
# Explanation:
# Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        
        for i in range(len(title)):
            word = title[i]
            if len(word) < 3:
                title[i] = word.lower()
            else:
                title[i] = word.title()
        
        return " ".join(title)