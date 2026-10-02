//================================
// Working process:
//   1. Iterate through the string s
//   2. If the character is an opening bracket, push it onto the stack
//   3. If the character is a closing bracket, check if the stack is empty
//      - If the stack is empty, return false (unmatched closing bracket)
//      - If the stack is not empty, check if the top of the stack matches the closing bracket
//          - If it matches, pop the top of the stack
//          - If it doesn't match, return false (mismatched brackets)
//   4. After iterating through the string, check if the stack is empty
//      - If the stack is empty, return true (all brackets matched)
//      - If the stack is not empty, return false (unmatched opening brackets)
// TakeAway: Learning to use a stack to validate parentheses and using unordered_map to store the pairs of brackets for easy lookup using C++.
//================================


class Solution {
public:
    bool isValid(string s) {
        std::stack<char> open;
        std::unordered_map<char, char> pairs = {
            {'(',')'}, {'{','}'}, {'[',']'}
        };

        for(const char& str: s){
            if(pairs.contains(str)){
                open.push(str);
            }
            else{
                if(open.empty()){
                    return false;
                }
                else{
                    if(pairs[open.top()] == str){
                        open.pop();
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        if(open.empty()){
            return true;
        }

        return false;
    }
};