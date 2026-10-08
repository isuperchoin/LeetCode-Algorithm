//================================
// Working process:
//   1. Iterate through nums once
//   2. Calculate comp as the difference between target and the current element
//   3. If comp is already in the unordered_map pairs, return its index and the current index
//   4. Otherwise, store the current element as a key with its index as the value
// Issue: variable comp is declared outside the for loop, which can lead to confusion and potential bugs if the variable is used elsewhere in the code.
//================================


#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> pairs;
        int comp;

        for(int i{0}; i<nums.size(); ++i){
            comp = target - nums[i];
            if(pairs.contains(comp)){
                return std::vector<int> {pairs[comp],i};
            }
            else{
                pairs[nums[i]] = i;
            }
        }

        return std::vector<int> {};
    }
};