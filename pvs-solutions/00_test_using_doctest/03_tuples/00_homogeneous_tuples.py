'''
  This file lists tests for automated testing of tuples in Python

  The below automated test teaches how reporting of a tuple in Python tuple looks like
  NOTE : Observe the difference between using it is as a LIST and as a TUPLE
>>> tuple1
(1, 2, 3, 4)

  The below automated test illustrates how to find an element (say, element '3')
  by index within a tuple
>>> elementValue3
3

  The below automated test illustrates that a homogeneous tuple could contain other tuples as well
>>> tuple2
(5, 6, (1, 2, 3, 4))

  The below automated test demonstrates how to find element of a nested tuple (say, element '4')
>>> elementValue4
4

  The below automated test illustrates new tuples could be formed as a result of addition
  of other tuples
>>> tuple3
(1, 2, 3, 4, 5, 6, (1, 2, 3, 4))

  The below automated test illustrates multiplication of a tuple (tuple1) with a SCALAR
>>> tuple1_multiply_by_2_demo
(1, 2, 3, 4, 1, 2, 3, 4)

  The below automated test illustrates how to embed a list within a tuple
>>> tuple4
(1, 2, 3, 4, [5, 6, 7, 8])

  The below automated test illustrates how to find an element within a list
  embedded within a tuple
>>> elementValue8
8

  NOTE :
    The elements of a tuple are IMMUTABLE whereas elements of a list are MUTABLE.

'''

## Import libraries here
import sys

# Start writing up the new code from here
# Start fixing up the broken code from here
tuple1 = (1, 2, 3, 4)
elementValue3 = tuple1[2]

tuple2 = (5, 6, tuple1)
elementValue4 = tuple2[2][3]

tuple3 = tuple1 + tuple2
tuple1_multiply_by_2_demo = tuple1 * 2

list1 = [5, 6, 7, 8]
tuple4 = (1, 2, 3, 4, list1)

elementValue8 = tuple4[4][3]

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
