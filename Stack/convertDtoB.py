#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:40:00 2020

@author: xuyingwang
"""
from Stack import Stack

def convert_decimal_binary(num):
    stack = Stack()
    
    if num == 0:
        return num
    
    while num > 0:
        reminder = num % 2
        stack.push(reminder)
        num = num // 2
        
    binary_num = ""
    while not stack.is_empty():
        binary_num += str(stack.pop())
        
    return binary_num

print(convert_decimal_binary(252))