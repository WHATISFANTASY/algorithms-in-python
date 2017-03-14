#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def F(x):
    if x == 0 or x == 1:
        return 1
    return F(x - 1) + F(x - 2)

f = F(5)
print(f)
