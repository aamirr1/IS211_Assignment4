#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Part-2 """

import random
import time


def insertion_sort(exp1):
    """ List of numbers """
    
    begin = time.time()
    for index in range(1, len(exp1)):

        current_value = exp1[index]
        position = index

        while position > 0 and exp1[position - 1] > current_value:
            exp1[position] = exp1[position - 1]
            position = position - 1
            exp1[position] = current_value
        last = time.time()
        
        return exp1, last-begin


def shell_sort(exp1):
    """ shell_sort function """
    
    begin = time.time()
    sublist_count = len(exp1) // 2

    while sublist_count > 0:
        for begin_position in range(sublist_count):
            another_insertion_sort(exp1, begin_position, sublist_count)
        sublist_count = sublist_count // 2
    last = time.time()
    
    return exp1, last-begin


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
    
    begin = time.time()
    exp1.sort()
    last = time.time()
    
    return exp1, last-begin

def random_number(exp3):
    """ randon function """
    
    random_list = random.sample(range(0, exp3), exp3)
    return random_list


def main():
    """ main function """
    
    list = {'list1': 500,
             'list2': 1000,
             'list3': 10000}
    for var in list.values():
        random_list = random_number(var)
        iter_count = 100
        output = {'insertion':0,
                  'shell_sort':0,
                  'python_sort':0}
        while iter_count > 0:
            output['insertion'] += insertion_sort(random_list)[1]
            output['shell_sort'] += shell_sort(random_list)[1]
            output['python_sort'] += python_sort(random_list)[1]
            iter_count -= 1

        print "List of %s length the var timed:" % var
        print "Insertion Sort took %10.7f seconds to run on average" % \
              (float(output['insertion'] / 100))
        print "Shell Sort took %10.7f seconds to run on average" % \
              (float(output['shell_sort'] / 100))
        print "Python Sort took %10.7f seconds to run on average" % \
              (float(output['python_sort'] / 100))
        print '\n'

if __name__ == '__main__':
    main()
