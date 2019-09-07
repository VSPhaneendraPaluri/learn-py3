'''
  This file lists tests for automated testing of homogenous lists in Python

  The following automated tests teach how reporting of a homogenous Python list looks like
>>> list1
[1, 2, 3, 4]
>>> list2
[5, 6, 7, 8]

  The below test demonstrate the add operations on lists
>>> lists_add_demo
[1, 2, 3, 4, 5, 6, 7, 8]

  The below test demonstrates the slicing operations on lists.
>>> list3_sliced_from_list1
[3, 4]

  The below test demonstrates the copy by reference of list3_sliced_from_list1
>>> list3
[3, 4]

  The below test demonstrates the multiplation operations on list3 by 3.
>>> list3_multiply_by_3_demo
[3, 4, 3, 4, 3, 4]

  The below test demonstrates copy by value of list3
  NOTE :  Note the difference in 'copy by reference' and 'copy by value'
>>> list4
[3, 4]

  The below test demonstrates adding an element to a list (say, list4) using 'append'
  NOTE : 
    1. Notice the need for copy by value (again!)
    2. Observe the need for the temporary list
>>> list5
[3, 4, 10]

'''

## Import libraries here
import sys

# Start writing up the new code from here
# Start fixing up the broken code from here
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
lists_add_demo = list1 + list2
list3_sliced_from_list1 = list1[2:]
list3 = list3_sliced_from_list1
list3_multiply_by_3_demo = list3 * 3
list4 = list(list3)
list5_temp = list(list4)
list5_temp.append(10)
list5 = list5_temp

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
