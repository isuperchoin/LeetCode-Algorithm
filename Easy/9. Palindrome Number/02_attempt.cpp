//================================
// Working process:
//   1. Iterate through the first half of the string representation of x.
//   2. Compare the characters at the current index and the corresponding index from the end of the string.
//   3. If they are not equal, return false.
//   4. If the loop completes without returning false, return true.
// Refinement: The code converts the integer x to a string once and stores it in a variable, which improves efficiency and readability.
// TakeAway: Learning to write code in C++ and using string manipulation to check for palindromes.
//================================


class Solution {
public:
    bool isPalindrome(int x) {
        std::string s = std::to_string(x);

        for(int i=0;i<s.size()/2;++i){
            if(s[i] != s[s.size()-1-i]){
                return false;
            }
        }

        return true;
    }
};