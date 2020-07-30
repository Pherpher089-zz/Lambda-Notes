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

# Find Numbers with Even Number of Digits

### Given an array `nums` of integers, return how many of them contain an even number of digits.

### Example:

    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore only 12 and 7896 contain an even number of digits.

### Constraints

-   1 <= nums.length <= 500
-   1 <= nums[i] <= 10^5

## My Solutions

> 1st Solution

```Java
class Solution {
    public int findNumbers(int[] nums) {
        int evenCount = 0;
        for(int i = 0; i<nums.length; i++) {
            String number = Integer.toString(nums[i]);
            if(number.length() % 2 == 0){
                evenCount++;
            }
        }
        return evenCount;
    }
}
```

# Squares of a Sorted Array

### Description:

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

Example 2:

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

#### Solution 1:

```Java
class Solution {
    public int[] sortedSquares(int[] A) {
        for(int i = 0; i < A.length; i++) {
            A[i] = A[i] * A[i];
            System.out.println(A[i]);
        }
        Arrays.sort(A);
        return A;
    }
}
```

This is totally the brute force method. The over all runtime for this solution is `O(N log N)` and space complexity in this case is `O(1)`. There is a better, two pointer solution.
