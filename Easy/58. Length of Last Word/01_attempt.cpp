//================================
// Working process:
//   1. Iterate through the string s from the end to the beginning.
//   2. Keep track of the length of the last word encountered.
//   3. If a space is encountered and the length is not zero, return the length.
//   4. If a non-space character is encountered, increment the length.
// TakeAway: Learning to write code in C++ and using a simple loop to find the length of the last word in a string.
//================================


class Solution {
public:
    int lengthOfLastWord(string s) {
        int length{0};
        for(int i = s.size()-1; i >= 0; --i){
            if(s[i] == ' '){
                if(length != 0){
                    return length;
                }
            }
            else{
                ++length;
            }
        }
        return length;
    }
};