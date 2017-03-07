#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Part-1 """

import random
import time

def sequential_search(exp1, exp2):
    """ Search for sequent """
    
    begin = time.time()
    post = 0
    result = False

    while post < len(exp1) and not result:
        if exp1[post] == exp2:
            result = True
        else:
            post = post + 1

    last = time.time()
    return result, last-begin


def ordered_sequential_search(exp1, exp2):
    """ Search for ordered sequent """
    
    begin = time.time()
    post = 0
    result = False
    stop = False
    while post < len(exp1) and not result and not stop:
        if exp1[post] == exp2:
            result = True
        else:
            if exp1[post] > exp2:
                stop = True
            else:
                post = post+1

    last = time.time()
    return result, last-begin


def binary_search_iterative(exp1, exp2):
    """ Search for binary iterative"""
    
    begin = time.time()
    exp1.sort()
    first = 0
    last = len(exp1) - 1
    result = False

    while first <= last and not result:
        y = (first + last) // 2

        if exp1[y] == exp2:
            result = True
        else:
            if exp2 < exp1[y]:
                last = y - 1
            else:
                first = y + 1

    last = time.time()
    return result, last-begin


def random_gen(exp3):
    """ Generate random"""
    
    random_list = random.sample(range(0, exp3), exp3)
    return random_list


def binary_search_recursive(exp1, exp2):
    """ Search binary recursive """
    
    begin = time.time()
    exp1.sort()

    if len(exp1) == 0:
        result = False
    else:
        y = len(exp1) // 2

        if exp1[y] == exp2:
            result = True
        else:
            if exp2 < exp1[y]:
                return binary_search_iterative(exp1[:y], exp2)
            else:
                return binary_search_iterative(exp1[y + 1:], exp2)

    last = time.time()
    return result, last-begin



def main():
    """ This function returns a full results """
    
    list = {'list1': 500,
             'list2': 1000,
             'list3': 10000}

    for var in list.values():
        random_list = random_gen(var)
        iter_count = 100
        output = {'sequential':0,
                  'ordered_seq':0,
                  'binary_seq':0,
                  'binary_recur':0}
        while iter_count > 0:
            output['sequential'] += sequential_search(random_list, -1)[1]
            output['ordered_seq'] += ordered_sequential_search(random_list, -1)[1]
            output['binary_seq'] += binary_search_iterative(random_list, -1)[1]
            output['binary_recur'] += binary_search_recursive(random_list, -1)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % var

        print "Sequential took %10.7f seconds to run on average" % \
              (float(output['sequential']/ 100))
        print "Ordered Seq took %10.7f seconds to run on average" % \
              (float(output['ordered_seq'] / 100))
        print "Binary Iter took %10.7f seconds to run on average" % \
              (float(output['binary_seq']/ 100))
        print "Binary Recur took %10.7f seconds to run on average" % \
        (float(output['binary_recur']/ 100))
        print '\n'


if __name__ == '__main__':
    main()
