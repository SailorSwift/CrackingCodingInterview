#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:16:53 2020

@author: xuyingwang
"""

# A definition of stack: just like stack a few books on top
# of each then, when you try to take them out, list in last out.
# you can only take one item off at a time
# you can peek the top of the stack


class Stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
        
    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items
        