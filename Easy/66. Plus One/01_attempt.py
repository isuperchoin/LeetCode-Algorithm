#================================
# Working process:
#   1. Join digits into a string and turn that into integer
#   2. Add 1 to it
#   3. Turn it into a string and split into list
#   4. Turn each elemnts of the list into integers
#   5. return the list
#  Issue: No takeaways, relies too much on python library and not the algorithm itself
#================================


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        return list(map(int,list(str(int(''.join(map(str, digits)))+1))))
        