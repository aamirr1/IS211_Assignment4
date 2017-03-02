#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Assignment 4 part-2"""

import random
import time


def insertion_sort(exp1):
    """ List of numbers """
    
    start = time.time()
    for index in range(1, len(exp1)):

        current_value = exp1[index]
        position = index

        while position > 0 and exp1[position - 1] > current_value:
            exp1[position] = exp1[position - 1]
            position = position - 1
            exp1[position] = current_value
        end = time.time()
        
        return exp1, end-start


def shell_sort(exp1):
    """ shell_sort function """
    
    start = time.time()
    sublist_count = len(exp1) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            another_insertion_sort(exp1, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    
    return exp1, end-start


def another_insertion_sort(exp1, exp2, exp4):
    """ another_insertion_sort """
    
    for i in range(exp2 + exp4, len(exp1), exp4):
        current_value = exp1[i]
        position = i
        while position >= exp4 and exp1[position - exp4] > current_value:
            exp1[position] = exp1[position - exp4]
            position = position - exp4
        exp1[position] = current_value


def python_sort(exp1):
    """ pythin_sort function """
    
    start = time.time()
    exp1.sort()
    end = time.time()
    
    return exp1, end-start

def random_number(exp3):
    """ randon function """
    
    random_list = random.sample(range(0, exp3), exp3)
    return random_list


def main():
    """ main function """
    
    tests = {'test1': 500,
             'test2': 1000,
             'test3': 10000}
    for test in tests.values():
        random_list = random_number(test)
        iter_count = 100
        output = {'insert':0,
                  'shell':0,
                  'pyth':0}
        while iter_count > 0:
            output['insert'] += insertion_sort(random_list)[1]
            output['shell'] += shell_sort(random_list)[1]
            output['pyth'] += python_sort(random_list)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test
        print "Insertion Sort took %10.7f seconds to run on average" % \
              (float(output['insert'] / 100))
        print "Shell Sort took %10.7f seconds to run on average" % \
              (float(output['shell'] / 100))
        print "Python Sort took %10.7f seconds to run on average" % \
              (float(output['pyth'] / 100))
        print '\n'

if __name__ == '__main__':
    main()
