//================================
// Working process:
//   1. Determine the shortest string in the input vector of strings.
//   2. Iterate through the characters of the shortest string.
//   3. For each character, compare it with the corresponding character in all other strings.
//   4. If a mismatch is found, return the substring of the shortest string up to that index.
//   5. If no mismatch is found, return the entire shortest string as the longest common prefix.
// Refinement: The for loop now uses a reference to avoid creating copies of the strings in the vector, which improves efficiency.
// TakeAway: Learning to write code in C++ and using string manipulation to find the longest common prefix among a vector of strings.
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
            for(const std::string& str:strs){
                if(str[i] != strs[0][i]){
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0].substr(0, min_it->size());
    }
};