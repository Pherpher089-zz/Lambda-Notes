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

# Duplicate Zeros

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

```Java
class Solution {
    public void duplicateZeros(int[] arr) {
        
        int counter = 1; // Used to count spaces based on zero or !zero values
        int index = 0; // Holds the current index we are searching
        int tailIndex = arr.length- 1; // Used to track the index we are replacing
        
        while(counter < arr.length) {
            if(arr[index] == 0) {
                counter += 2;
            } else {
                counter++;
            }
            index++;
        }
        
        while(tailIndex > 0) {
            System.out.println(tailIndex + ": " + arr[tailIndex]);
            System.out.println(index + ": " + arr[index]);
            System.out.println("");
            if(arr[index] == 0) {
                arr[tailIndex] = 0;
                arr[tailIndex - 1] = 0;
                tailIndex -= 2;
                index--;
            } else {
                arr[tailIndex] = arr[index];
                tailIndex--;
                index--;
                
            }
        }
    }
}
```

First pass solution (does not work). There is an issue if: the counter pointer lands on a zero && there is an odd number of no zero values before the counter

`08-20-2020`

So I reviewed the discussion for my solution and It appears that using another array is indeed the correct way to do this. I am assigning the correct values to a new array and reassigning that the current i index to the old array.

```JAVA
class Solution {
    public void duplicateZeros(int[] arr) {
        int pointer = 0;
        int newArr[] = new int[arr.length];
        for(int i = 0; i < arr.length; i++) {
            if(pointer < arr.length){
                if(arr[i] == 0) {
                newArr[pointer] = 0;
                if(pointer+1 < arr.length) {
                    newArr[pointer + 1] = 0;
                }
                pointer += 2;
                } else { 
                    newArr[pointer] = arr[i];
                    pointer++;
                }
            }
            arr[i] = newArr[i]; 
        }
    }
}
```


>   **Runtime:** O(N) - 100% of submissions


>   **Space Complexity:** O(N) - 91% of submissions. 


>   **Return Goal**: N(1) space complexity

# Merge Sorted Array

### First Pass solution

While this works perfectly at 0ms, it is not the best on space complexity. The issue that the third array addresses is the fact that I don't want to overwrite the first elements before they are copied back into the array. A solution that I seen was to build it backward in descending order. I will try to replicate this solution from my memory. 

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Take the elements of nums2 and input them into nums1
        //INITAL IDEA: Duplicate the first m - n elements of nums 1 and sort them back into Nums1
        
        //Create place holder array
        //assign place holder array
        //create two pointers for each separate array
        
        //loop through nums1
            //decide between both pointed values
            //asign value to nums1
            //incrament the correct pointer
        int nums3[] = new int[m];
        int p2 = 0, p3 = 0;
        for(int i = 0; i < nums3.length; i++) {
            nums3[i] = nums1[i];
        }
        
        for(int i = 0; i < nums1.length; i++) {
            if(p2 < nums2.length && p3 < nums3.length){
                if(nums2[p2] < nums3[p3]) {
                    nums1[i] = nums2[p2];
                    p2++;
                } else {
                    nums1[i] = nums3[p3];
                    p3++;
                }
            }  else if(p2 < nums2.length) {
                nums1[i] = nums2[p2];
                p2++;
            } else {
                nums1[i] = nums3[p3];
                p3++;
            }
        }
        
    }
}
```

> Runtime: O(n) - 0ms - 100%

> Space Complexity: O(n) - 39.7mb - 58%

### Second Pass: Focus on space saving
This only gets me a few more percent on overall submissions. Much cleaner though. 

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n -1;
        int k = m + n - 1;
        int a,b;
        
        while(i >= 0 || j >= 0) {
            a = i >= 0 ? nums1[i] : Integer.MIN_VALUE;
            b = j >= 0 ? nums2[j] : Integer.MIN_VALUE;
            
            nums1[k--] = Math.max(a,b);
            if(a>b){
                i--;
            } else {
                j--;
            }
        }
    }
}
```
> Runtime: O(n) - 0ms - 100%
> 
> Space Complexity: O(n) - 39.6mb - 58%