// Leetcode 367 Easy
// By Xinhai Wei, on Jan 20th, 2020

// The code shall mean no academic offense to any source website.

// Description: 
// Given a positive integer num, 
// write a function which returns True if num is a perfect square else False.

class Solution {
public:
    bool isPerfectSquare(int num) {
        int i = 0;
        while(i * i <= num){
            if(i * i == num){
                return true;
            }
            if(i < 46340){
                ++i;
            } else {
                return false;
            }
        }
        return false;
    }
};
