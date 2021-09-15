#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    ans = ''
    while node:
        ans += (str(node.data))
        node = node.next
        if node:
            ans += sep
    print(ans)


# Complete the mergeLists function below.


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    mList = SinglyLinkedList()

    while (head1 or head2):
        if head1:
            if head2:
                if (head1.data > head2.data):
                    mList.insert_node(head2.data)
                    head2 = head2.next
                else:
                    mList.insert_node(head1.data)
                    head1 = head1.next
                
            else:
                mList.insert_node(head1.data)
                head1 = head1.next
        else:
            mList.insert_node(head2.data)
            head2 = head2.next
    return mList.head


if __name__ == '__main__':

    tests = 1

    for tests_itr in range(tests):

        llist1 = SinglyLinkedList()
        llist1.insert_node(1)
        llist1.insert_node(2)
        llist1.insert_node(3)

        llist2 = SinglyLinkedList()
        llist2.insert_node(3)
        llist2.insert_node(4)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, '  ')
