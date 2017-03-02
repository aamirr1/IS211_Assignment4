#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Assignment 4 part-1"""

import random
import time



def sequential_search(exp1, exp2):
    """ Search for sequent """
    
    start = time.time()
    pos = 0
    found = False

    while pos < len(exp1) and not found:
        if exp1[pos] == exp2:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end-start


def ordered_sequential_search(exp1, exp2):
    """ Search for ordered sequent """
    
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(exp1) and not found and not stop:
        if exp1[pos] == exp2:
            found = True
        else:
            if exp1[pos] > exp2:
                stop = True
            else:
                pos = pos+1

    end = time.time()
    return found, end-start


def binary_search_iterative(exp1, exp2):
    """ Search for binary iterative"""
    
    start = time.time()
    exp1.sort()
    first = 0
    last = len(exp1) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if exp1[midpoint] == exp2:
            found = True
        else:
            if exp2 < exp1[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start


def binary_search_recursive(exp1, exp2):
    """ Search binary recursive """
    
    start = time.time()
    exp1.sort()

    if len(exp1) == 0:
        found = False
    else:
        midpoint = len(exp1) // 2

        if exp1[midpoint] == exp2:
            found = True
        else:
            if exp2 < exp1[midpoint]:
                return binary_search_iterative(exp1[:midpoint], exp2)
            else:
                return binary_search_iterative(exp1[midpoint + 1:], exp2)

    end = time.time()
    return found, end-start


def random_gen(exp3):
    """ Generate random"""
    
    random_list = random.sample(range(0, exp3), exp3)
    return random_list


def main():
    """ This function returns a full results """
    
    tests = {'test1': 500,
             'test2': 1000,
             'test3': 10000}

    for test in tests.values():
        random_list = random_gen(test)
        iter_count = 100
        output = {'seq':0,
                  'ord_seq':0,
                  'bin_iter':0,
                  'bin_recur':0}
        while iter_count > 0:
            output['seq'] += sequential_search(random_list, -1)[1]
            output['ord_seq'] += ordered_sequential_search(random_list, -1)[1]
            output['bin_iter'] += binary_search_iterative(random_list, -1)[1]
            output['bin_recur'] += binary_search_recursive(random_list, -1)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test

        print "Sequential took %10.7f seconds to run on average" % \
              (float(output['seq']/ 100))
        print "Ordered Seq took %10.7f seconds to run on average" % \
              (float(output['ord_seq'] / 100))
        print "Binary Iter took %10.7f seconds to run on average" % \
              (float(output['bin_iter']/ 100))
        print "Binary Recur took %10.7f seconds to run on average" % \
        (float(output['bin_recur']/ 100))
        print '\n'


if __name__ == '__main__':
    main()
