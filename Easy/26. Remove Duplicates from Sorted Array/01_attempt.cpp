//================================
// Working process:
//   1. Iterate through the sorted array nums starting from the second element
//   2. Compare the current element with the previous one
//   3. If they are different, assign the current element to the position indicated by pointer and increment pointer
//   4. Continue until the end of the array
//   5. Return the value of pointer, which represents the length of the array without duplicates
// TakeAway: Learning to use a two-pointer technique to remove duplicates from a sorted array
//================================


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int pointer{1};

        for(int i = 1; i < nums.size(); ++i){
            if(nums[i] != nums[i-1]){
                nums[pointer] = nums[i];
                ++pointer;
            }
        }

        return pointer;
    }
};