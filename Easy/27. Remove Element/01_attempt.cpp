//================================
// Working process:
//   1. Iterate through the array nums
//   2. If the current element is not equal to val, assign it to the position indicated by pointer and increment pointer
//   3. Continue until the end of the array
//   4. Return the value of pointer, which represents the length of the array without the specified value
// TakeAway: Learning to use a two-pointer technique to remove all instances of a specific value from an array in-place with C++.
//================================


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        int pointer{0};

        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] != val){
                nums[pointer] = nums[i];
                ++pointer;
            }
        }

        return pointer;
    }
};