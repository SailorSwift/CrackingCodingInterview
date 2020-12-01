#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:13:26 2020

@author: xuyingwang
"""

from Stack import Stack

# =============================================================================
# s1 = Stack()
# print(s1.is_empty())
# s1.push("A")
# s1.push("B")
# s1.push("C")
# s1.push("D")
# print(s1.get_stack())
# print(s1.peek())
# 
# =============================================================================

# brackets only contains () [] {}
# the first thing we do to make sure and be able to compare

def is_match(open_b, close_b):
    if open_b == "(" and close_b == ")":
        return True
    elif open_b == "[" and close_b == "]":
        return True
    elif open_b == "{" and close_b == "}":
        return True
    else:
        return False
    
print(is_match("[", "]"))
print(is_match("[", "}"))

def is_brackets_valid(input_brackets):
    
    # this is based the input string is valid
    # first step in the algorithm is to iterate the input string,
    # if we encounter an open bracket, we put onto the stack
    
    stack = Stack()
    is_balanced = True
    index = 0
    
    while index < len(input_brackets) and is_balanced:
        bracket = input_brackets[index]
        # we need to find the open bracket, when we encounter an open bracket
        if bracket in "([{":
            stack.push(bracket)
        else:
            # it must be close bracket, then we need to pop it off the stack
            # this is the sepcail case, only closed brackets
            if stack.is_empty():
                is_balanced = False
            else:
                o_bracket = stack.pop()
                if not is_match(o_bracket, bracket):
                    is_balanced = False
        index += 1
        
    if stack.is_empty() and is_balanced == True:
        return True
    else:
        return False
    
print(is_brackets_valid("{}"))
print(is_brackets_valid("[({})"))
print(is_brackets_valid("[]{}()"))
print(is_brackets_valid("}}"))

     
        
            
    