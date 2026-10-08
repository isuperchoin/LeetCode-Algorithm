//================================
// Working process:
//   1. Determine the shortest string in the input vector of strings.
//   2. Iterate through the characters of the shortest string.
//   3. For each index, compare the character of every string with the character of strs[0] at that index.
//   4. If a mismatch is found, return the substring of the current string up to that index.
//   5. If no mismatch is found, return strs[0] up to the length of the shortest string as the longest common prefix.
// Issue: For loop creates a copy of each string in the vector, which can be inefficient.
//================================


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        auto min_it = std::min_element(
            strs.begin(),
            strs.end(),
            [](const std::string& a, const std::string& b){return a.size() < b.size();}
        );

        for(int i = 0; i< min_it->size(); ++i){
            for(std::string str:strs){
                if(str[i] != strs[0][i]){
                    return str.substr(0, i);
                }
            }
        }

        return strs[0].substr(0, min_it->size());
    }
};