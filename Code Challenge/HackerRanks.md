# Hacker Rank Challenges

## [Sherlock and Anagrams](https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps)

06/30/20

Start [`5:41pm`] -- End [`6:00pm`]

-   Was unable to come up with a solution using hash maps. I am going to look through the discussions next session.

07/1/20

Start [`11:44am`] -- End [`12:10pm`]

-   I gathered two quick hints from the top discussion thread. They were to traverse the string and find all of the possible substrings, Then check if the substrings of the same length match. I am going to try this approach

Start [`9:10pm`] end [`9:54`] -> SOLVED

```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    all_sub_srtrings = get_all_substrings(s)
    # print(all_sub_srtrings)
    count = 0
    i = 1
    while i in all_sub_srtrings:
        for idx, sub_dic in enumerate(all_sub_srtrings[i]):
            for j in range(idx+1, len(all_sub_srtrings[i])):
                if(all_sub_srtrings[i][j] == sub_dic):
                    count += 1
        i+=1

    print('count: {}'.format(count))
    return count

    # loop through every key in returned dic
        # compare each dictionary in the key and compare them

def get_all_substrings(s):
    # return a dic of dics with all possible substrings
    # the main dic will have a length as the key and a list of the possible substrings as dictionaries of that length as a value
    dic = {}
    length = len(s) - 1
    # print('lenght: {} len(s): {}'.format(length,len(s)))
    while length > 0:

        sub_strings = []
        counter = 0
        dic[length] = []
        # print('len(s) - length = {}'.format(len(s) - length))
        for i in range(len(s) - length + 1):
            # print('i: {}'.format(i))
            sub_dic = {}
            for j in range(length):
                if s[j+counter] in sub_dic:
                    sub_dic[s[j+counter]] += 1
                else:
                    sub_dic[s[j+counter]] = 0
            counter += 1
            dic[length].append(sub_dic)
        # print('length: {}'.format(length))
        length -= 1

    # print(dic)
    return dic



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

```

This was a tricky one. I had to create every single combination of sub strings as dictionaries. Then I dumped them into lists based on the sub string length. I then compared each dictionary to every other dictionary in the list and incremented a counter every time there was a match.

## [Count Triplets](https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps&isFullScreen=true&h_r=next-challenge&h_v=zen)

07/01/20

Start [`10:02pm`] -- End [`10:15pm`]

I understand the underlying goal for this algorithm but im seeing inherent issues with my own strategy and have yet to realize what the hashmap will be used for.

`current progress`

```python
def countTriplets(arr, r):
    triplets = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pass
```

7/06/20

Start [`7:03`pm] -- End [`7:52pm`]

```python
arr_dic = {}
    triplets = []

    print('here')
    def helper(triplet):
        target_value = arr[triplet[len(triplet) - 1]] * r
        if target_value in arr_dic:
            for i in arr_dic[target_value]:
                new_trip = triplet[:]
                new_trip.append(i)
                if len(new_trip) == 3:
                    triplets.append(new_trip)
                else:
                    helper(new_trip)
        else:
            return

    for i, j in enumerate(arr):
        if j not in arr_dic:
            arr_dic[j] = [i]
        else:
            arr_dic[j].append(i)

    for i in range(len(arr)):
        triplet = [i]
        print(len(triplets))
        helper(triplet)

    return len(triplets)
```

This solution passed all but four test cases. I don't think this solution is efficient enough. Upon looking through the discussions, I found some very helpful tips. I will attempt new, iterative solution tomorrow. Legend has it, it can be done with O(n), and a hash map is a must.

## [Reverse-integer](https://leetcode.com/problems/reverse-integer/)

7/8/20

Start [`10:18pm`] -- End [`???`]

## [running-sum-of-1d-array](https://leetcode.com/problems/running-sum-of-1d-array/)

7/15/20

Start [`1:39am`] -- End [`1:41am`]

Very simple problem, only took me several minuets

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            nums[i] += sum
            sum = nums[i]
        return nums

```

## [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

7/15/20

Start[`1:43`] -- End[`2:00`]

No problems here

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs += 1

        return good_pairs
```

attempted to refactor to lower runtime. Will pick back up in the morning
