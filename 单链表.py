#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 操作pop删除表头结点并返回这个结点里的数据
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        self._head = self._head.next
        return self._head.elem

    # 在表头插入数据
    def prepend(self, elem):
        self._head = LNode(elem)

    # 在链表最后插入元素
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return None
        # 如果链表为空则直接把表头指向需要插入的元素即可在。实际上是在操作_head域

        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        # 如果不为空，则先从头遍历链表，找到最后的结点，然后把最后结点的next指向需要插入的元素即可。实际上是在操作next域

    # 删除最后一个结点
    def pop_last(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop_last")

        p = self._head

        if p.next is None:  # 如果表长为1，则清空之，并返回原来的元素
            self._head = None
            return p.elem

        while p.next.next is not None:
            p = p.next
        p.next = None
        return p.next.elem
        # 如果表长大于1,则从头遍历，找到倒数第二个结点，把倒数第二个结点的next域置空，并返回最后一个结点

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
