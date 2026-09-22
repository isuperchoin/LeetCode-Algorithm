//================================
// Working process:
//   1. Iterate through nums
//   2. Iterate through nums once again from where we left off
//   3. Check if sum of those two elements of nums are equal to target
//   4. Return the indices if found
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