#!/usr/bin/python
# -*- coding: utf-8 -*- 

#冒泡排序
def maopao(nums):
    for i in range(1,len(nums)):
        for j in range (0,len(nums)-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

arr  = [1,23,4,23,66,3,7,9]

print(maopao(arr))