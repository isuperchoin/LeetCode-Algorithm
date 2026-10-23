//================================
// Working process:
//   1. Iterate through the array and check if the current element is greater than or equal to the target.
//   2. If it is, return the current index as the insert position.
//   3. If the loop completes without finding a suitable position, return the size of the array as the insert position.
//  Takeaway: Learning to use linear search to find the insert position in a sorted array with C++.
//================================


class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] >= target){
                return i;
            }
        }
        return nums.size();
    }
};