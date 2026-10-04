//================================
// Working process:
//   1. Iterate through the digits vector from the last element to the first
//   2. Add 1 to the current digit
//   3. If the current digit is not equal to 10, break the loop
//   4. If the current digit is equal to 10, set it to 0 and continue to the next digit
//   5. After the loop, check if the first digit is 0, which indicates that we have a carry-over and need to insert 1 at the beginning of the vector
// TakeAway: Learning to handle carry-over when adding one to a number represented as an array of digits, and using vector operations in C++ to manipulate the array.
//================================


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for(int i = digits.size()-1; i>=0; --i){
            digits[i] += 1;
            if(digits[i] != 10){
                break;
            }
            else{
                digits[i] = 0;
            }
        }
        if(digits[0]==0){
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};