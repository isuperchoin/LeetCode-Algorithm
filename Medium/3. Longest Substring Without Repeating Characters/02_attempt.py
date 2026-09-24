#================================
# Working process:
#   1. Use a sliding window approach to keep track of the longest substring without repeating characters
#   2. Use a dictionary to store the last seen index of each character
#   3. If a character is seen again, move the starting pointer of the window to the right of the last seen index of that character
#   4. Update the output with the maximum length of the current window
# Refinement: Instead of using a while loop to move the starting pointer, we can directly set it to the last seen index + 1, which is more efficient. Moreover, returning only the output is enough, no need to check if following_pointer is 0 or not.
# TakeAway: Understanding how to use the sliding window technique and the importance of optimizing pointer movements
#================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        following_pointer = 0
        seen = {}
        output = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= following_pointer:
                following_pointer = seen[s[i]] +1

            if i - following_pointer +1 > output:
                output = i - following_pointer +1
            seen[s[i]] = i

        return output