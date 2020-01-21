// Leetcode 645 Easy
// By Xinhai Wei, on Jan 20th, 2020

// The code shall mean no academic offense to any source website.

// Description: 
// Given an array nums representing the data status of this set after the error. 
// Your task is to firstly find the number occurs twice and then find the number that is missing.
// Return them in the form of an array.

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int length = nums.size();
        int index1 = 0;
        int index2 = 0;
        int v[10001];
        for(int i = 0; i < length; ++i){
            v[i] = 0;
        }
        for(int i = 0; i < length; ++i){
            v[nums[i]-1] += 1;
        }
        for(int i = 0; i < length; ++i){
            if(v[i] == 0){
                index2 = i+1;
            }
            if(v[i] == 2){
                index1 = i+1;
            }
        }
        nums.clear();
        nums.push_back(index1);
        nums.push_back(index2);
        return nums;
    }
};
