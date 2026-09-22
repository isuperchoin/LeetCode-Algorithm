
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