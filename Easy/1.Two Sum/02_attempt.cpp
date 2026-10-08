//================================
// Working process:
//   1. Iterate through nums once
//   2. Calculate comp as the difference between target and the current element
//   3. If comp is already in the unordered_map pairs, return its index and the current index
//   4. Otherwise, store the current element as a key with its index as the value
// Refinement: variable comp is declared inside the for loop to limit its scope and improve readability.
// TakeAway: Learning to write code in C++ and using unordered_map to store the pairs of numbers and their indices for faster lookup.
//================================


#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pairs;

        for(int i{0}; i<nums.size(); ++i){
            int comp = target - nums[i];
            if(pairs.contains(comp)){
                return {pairs[comp],i};
            }
            else{
                pairs[nums[i]] = i;
            }
        }

        return {};
    }
};