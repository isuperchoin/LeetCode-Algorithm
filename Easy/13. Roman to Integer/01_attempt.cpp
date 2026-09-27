//================================
// Working process:
//   1. Create an unordered_map to map Roman numeral characters to their integer values.
//   2. Iterate through the string s from the beginning to the second last character.
//   3. For each character, compare its value with the value of the next character.
//   4. If the current character's value is less than the next character's value, subtract the current character's value from the output.
//   5. Otherwise, add the current character's value to the output.
//   6. After the loop, add the value of the last character to the output.
// TakeAway: Learning to write code in C++ and using unordered_map to store the mapping of Roman numerals to integers for efficient lookup.
//================================


class Solution {
public:
    int romanToInt(string s) {
        std::unordered_map<char, int> dictionary = {
            {'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
        };

        int output{0};

        for(int i=0; i< s.size()-1; ++i){
            if (dictionary[s[i]] < dictionary[s[i+1]]){
                output -= dictionary[s[i]];
            }
            else{
                output += dictionary[s[i]];
            }
        }

        output += dictionary[s.back()];

        return output;

    }
};