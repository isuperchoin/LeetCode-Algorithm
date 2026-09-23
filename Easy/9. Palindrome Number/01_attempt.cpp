//================================
// Working process:
//   1. Declare a pointer variable to keep track of the last index of the string representation of the integer x.
//   2. Iterate through the first half of the string representation of x.
//   3. Compare the characters at the current index and the pointer index.
//   4. If they are not equal, return false.
//   5. If the loop completes without returning false, return true.
// Issue: The code converts the integer x to a string multiple times, which is inefficient. It would be better to convert it once and store it in a variable.
//================================


class Solution {
public:
    bool isPalindrome(int x) {
        int pointer = std::to_string(x).size()-1;

        for(int i=0;i<std::to_string(x).size()/2;++i){
            if(!(std::to_string(x)[i]==std::to_string(x)[pointer])){
                return false;
            }
            --pointer;
        }

        return true;
    }
};