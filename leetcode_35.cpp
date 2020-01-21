// Leetcode 35 Easy
// By Xinhai Wei, on Jan 20th, 2020

// The code shall mean no academic offense to any source website.

// Description: 
// Given a sorted array and a target value, 
// return the index if the target is found.
// If not, return the index where it would be if it were inserted in order.

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int length = nums.size();
        for(int i = 0; i < length; ++i){
            if(target == nums[i]) {
                return i;
            }
            if(target < nums[i]){
                return i;
            }
        }
        return length;
    }
};
