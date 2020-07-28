# Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.

## My Solutions

> 1st Attempt

```Java
//Java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int highestCount = 0;
        int count = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                count++;
            } else {
                if(count > highestCount){
                    highestCount = count;
                }
                count = 0;
            }
        }
        return highestCount;
    }
}
```

> 2nd Attempt

```Java
//Java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int highestCount = 0;
        int count = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                count++;
            }
            if(count > highestCount){
                    highestCount = count;
            }
            if(nums[i] != 1) {
                count = 0;
            }
        }
        return highestCount;
    }
}
```

The issue was with the conditions. Before, `highestCount` had no chance to be assigned unless `nums[i] != 1`. This needed to happen no matter what. Also, `count` could only be reset when `nums[i] == 0` and highestCount was being reassigned.
