#================================
# Working process:
#   1. Use a sliding window approach to keep track of the longest substring without repeating characters
#   2. Use a dictionary to store the last seen index of each character
#   3. If a character is seen again, move the starting pointer of the window to the right of the last seen index of that character
#   4. Update the output with the maximum length of the current window
# Issue: While loop is used to move the starting pointer, which can be inefficient if there are many repeating characters, returning only the output is enogh, no need to check if following_pointer is 0 or not
#================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        following_pointer = 0
        seen = {}
        output = 0

        for i in range(len(s)):
            if s[i] in seen:
                while seen[s[i]] >= following_pointer:
                    following_pointer += 1

            if i - following_pointer +1 > output:
                output = i - following_pointer +1
            seen[s[i]] = i

        return output if following_pointer != 0 else len(s)