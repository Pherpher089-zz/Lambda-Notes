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

#### Solution 2

```Java
class Solution {
    public int[] sortedSquares(int[] A) {
    //My two pointer solution
        int[] output = new int[A.length];
        int p1 = 0, p2 = 0, counter = 0;

        //Find the pivot between negitive and non-negitive
        while(p2 < A.length && A[p2] < 0)
            p2++;
        p1 = p2 - 1;

        //Assign the array starting from the pivot out
        while(p1 >= 0 && p2 < A.length) {
            if(A[p1] * A[p1] > A[p2] * A[p2]) {
                output[counter++] = A[p2] * A[p2];
                p2++;
            } else {
                output[counter++] = A[p1] * A[p1];
                p1--;
            }
        }

        while(p2 < A.length) {
            output[counter++] = A[p2] * A[p2];
            p2++;
        }

        while(p1 >= 0) {
            output[counter++] = A[p1] * A[p1];
            p1--;
        }

        return output;
    }
}
```

This solution is quite a bit more tricky. Your looking at two pointers. One for the positive numbers and one for the negative. Which pointed absolute value is lower is squared and added to the output array and it's pointer is moved in it's respective direction. There is a little bit of logic set in to adjust when the pointers are out of range.

# Duplicate Arrays

Given a fixed length array `arr` of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array **in place**, do not return anything from your function.

**Example 1:**
**Input:** [1,0,2,3,0,4,5,0]
**Output:** null
**Explanation:** After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

**Example 2:**
**Input:** [1,2,3]

**Output:** null
**Explanation:** After calling your function, the input array is modified to: [1,2,3]
