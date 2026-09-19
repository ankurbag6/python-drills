"""
DESCRIPTION (inspired by Leetcode.com)
Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle.

For three sides to form a valid triangle, 
all three of these conditions must hold: 
(a + b > c), (a + c > b), and (b + c > a), 
where (a), (b), and (c) are the side lengths. 
In other words,
 the sum of every possible pair must exceed the third side.

nums = [11,4,9,6,15,18]
10

4, 15, 18
6, 15, 18
9, 15, 18
11, 15, 18
9, 11, 18
6, 11, 15
9, 11, 15
4, 9, 11
6, 9, 11
4, 6, 9

sort : [4 6 9 11 15 18]
        p            q
4,18 > 

"""

def triangleNumber(nums) -> int:
    nums.sort()
    count = 0
    for i in range(len(nums) - 1, 1, -1):   # i = largest side, walks down to index 2
        left = 0
        right = i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    return count


print(triangleNumber([11,4,9,6,15,18]))