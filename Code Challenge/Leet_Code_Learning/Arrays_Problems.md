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
> Space Complexity: O(n) - 39.6mb - 63.89%

# Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.

### My first solution
This is an adequate submission. I don't think this is a particularly hard problem to solve but I am totally satisfied with this answer.

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int spacer = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == val) {
                spacer++;
            } else {
                nums[i - spacer] = nums[i];
            }
        }
        return nums.length - spacer;
    }
}
```
The only improvement would be to reduce the space complexity but I've only defined one variable so im like whaaaa?

>   Runtime: 1ms - O(n) - 100%
>  Space Complexity: 39mb - O(n) - %15

# removing duplicates from sorted array
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### First pass solution

Clearly I didn't read the description of this problem well enough, because my solution is supper slow. I used a hash map and this would work for an unsorted array but for a sorted array, this is slow. I will try again tomorrow. 

```java
import java.util.*;

class Solution {
    public int removeDuplicates(int[] nums) {
        Dictionary<Integer, Integer> dupes = new Hashtable<Integer,Integer>();
        int counter = 0;
        
        for(int i = 0; i < nums.length; i++) {
            if(dupes.get(nums[i]) != null) {
                counter++;
            } else {
                dupes.put(nums[i], 0);
                nums[i - counter] = nums[i];
            }
        }
        
        System.out.println(dupes);
        return nums.length - counter;
    }
}
```
> Runtime: 8ms- O(N) -  7.23%
> Space complexity: O(N) - 40.8mb - 99.15% 

# Check If N and Its Double Exist

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

## First pass - No solution

```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm = {}
        for i in range(len(arr)):
            if arr[i] not in hm:
                hm[arr[i]] = i
            if arr[i] * 2 in hm:
                return True
            if (arr[i] / 2) % 1 == 0.0:
                if arr[i]/2 in hm:
                    return True
        return False
```
This solution is good except for when there are negative numbers in the data. I'm gunna throw a little more logic in here to see if I can get this to work. 

## First Pass - Refined 
```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm = {}
        for i in range(len(arr)):
            
            if arr[i] not in hm:
                hm[arr[i]] = i
            if arr[i] * 2 in hm and hm[arr[i]*2] != i:
                return True
            if (arr[i] / 2) % 1 == 0.0:
                if arr[i]/2 in hm and hm[arr[i]/2] != i:
                    return True
        return False
```
The problem was not the negative number, it was the element `0` existing in the array. This threw everything off. I have made a quick check for both if statements to prevent this from happening.


>   Runtime: 72ms - O(n) - 44.51%

>  Space Complexity: 13.9mb - O(n) - 44.65%

It appears that this can be done much quicker. I will attempt that tomorrow.

# Valid Mountain Array


Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

- A.length >= 3
- There exists some i with 0 < i < A.length - 1 such that:
  - A[0] < A[1] < ... A[i-1] < A[i]
  - A[i] > A[i+1] > ... > A[A.length - 1]

## First Pass Solution(success)

```Java
class Solution {
    public boolean validMountainArray(int[] A) {
        boolean peak = false;
        for(int i =0; i < A.length - 1; i++) {
            if(A[i] == A[i+1]) {
                return false;
            }
            
            if(A[i] < A[i+1] && peak){
                return false;
            } 
            
            if(A[i] > A[i+1] && !peak) {
                if(i > 0){
                    peak = true;    
                } else {
                    return false;
                }
                
            }
        }
        if(!peak) {
            return false;
        }
        return true;
    }
}
```
This is O(N) and uses a little memory but it was clean and quick. Will investigate better solutions for my information.

> Runtime 2ms 55.32% 
> Space 39.9 MB 97.72%

Not hating these results.


# Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

## Fist Pass Solution(accepted)
```java
class Solution {
    
    public int greatestValueIndex(int[] arr, int start) {
        //System.out.println("Finding greatest value index starting at " + start);
        int target = start;
        for(int i = start; i < arr.length; i++) {
            if(arr[i] > arr[target]) {
                target = i;
            }
        }
        //System.out.println("target found = " + target);
        return target;
    }
    
    public int[] replaceElements(int[] arr) {
        int j = greatestValueIndex(arr, 0);
        
        for(int i = 0; i < arr.length; i++) {
            if(i == arr.length - 1) {
                arr[i] = -1;
                break;
            }
            
            if(i >= j) {
                j = greatestValueIndex(arr, i+1);
            }
            //System.out.println("index " + i + " is now " + arr[j]);
            arr[i] = arr[j];
        }
        
        return arr;
    }
    
}
```

>   Runtime: 2ms 46.72% of submitions
> Space: 40MB 78.80% of submitions

Not supper disappointed with how quickly I came up with this solution. It's kinda a dynamic programming approach. 

# Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


## First pass Solution(Unaccepted)
```java
class Solution {
    public void moveZeroes(int[] nums) {
        int zeros = 0;
        for(int i = 0; i < nums.length; i++) {
            //System.out.println("zeros = " + zeros);
            //System.out.println("i = " + i);
            //System.out.println("nums[i-zeros] = " + nums[i-zeros]);
            //System.out.println("nums[i] = " + nums[i]);
            if(nums[i] == 0){
                zeros++;
            } else {
                nums[i-zeros] = nums[i];
                if(i >= nums.length - zeros) {
                    nums[i] = 0;  
                }
            }
            //System.out.println(Arrays.toString(nums));
            //System.out.println('\n');
        }
    }
}
```
This may take a backward approach to filling it in. So far the issue is that if there are zeros past the `nums.length - zeros` index, they are not accounted for and there for not written. We will try again tomorrow. 

## Second pass solution(accepted)

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int zeros = 0;
        for(int i = 0; i < nums.length + zeros; i++) {
            //System.out.println("zeros = " + zeros);
            //System.out.println("i = " + i);
            //System.out.println("nums[i-zeros] = " + nums[i-zeros]);
            //System.out.println("nums[i] = " + nums[i]);
            if(i < nums.length) {
                if(nums[i] == 0){
                    zeros++;
                } else {
                    nums[i-zeros] = nums[i];
                    if(i >= nums.length - zeros) {
                        nums[i] = 0;  
                    }
                }
            } else {
                System.out.println(nums.length - (nums.length + zeros - i));
                nums[nums.length - (nums.length + zeros - i)] = 0;
            }
            //System.out.println(Arrays.toString(nums));
            //System.out.println('\n');
        }
    }
}
```

>   Runtime: 5ms 09.95% of submissions
>   Space: 40MB 39.98% of submissions

This solution is a tad bit more than O(N). The runtime is very bad. I peeked at the quicker solution and will give that a try.

>   Hint Hint !!! I will atempt to rewrite this solution

```java
    public void moveZeroes(int[] nums) {
        //[0,1,0,3,12] --> [1,0,0,3,12] --> 1,3,0,0,12 -->   [1,3,12,0,0]
        //101 --110
        int wp=0;
        int temp=0;
        
        for (int rp=0 ; rp < nums.length-1 ; rp++){
            
            if (nums[rp]==0 && nums[rp+1] !=0 ){
                temp = nums[rp+1];
                nums[rp+1] =nums[rp]  ;
                nums[wp]=temp;
                wp++;
            }
            else if (nums[rp+1]==0 && nums[rp] !=0 ){
                 wp++;
            }
            else if (nums[rp+1] !=0 && nums[rp] !=0 )
                wp++;
        }        
    }
}
```