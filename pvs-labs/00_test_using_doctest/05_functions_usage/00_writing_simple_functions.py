'''
  This tutorial would help the users understand the right syntax that
  are possible with functions usage in Python

  This automated test shall enable the function to print first five
  natural numbers
>>> print_natural_numbers(3)
[1, 2, 3]
>>> print_natural_numbers(5)
[1, 2, 3, 4, 5]


  This automated test shall enable the function to take in an argument
  and generates odd number not exceeding the input argument
>>> generate_odd_numbers(10)
[1, 3, 5, 7, 9]
>>> generate_odd_numbers(20)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

  NOTE :  There could be multiple implementations to achieve the objective
  
'''

# Import Python modules here
import sys


# Start writing up the new code from here
# Start fixing up the broken code from here

def print_natural_numbers(max_count):
  n_list = []
  return n_list


def generate_odd_numbers(max_odd_number):
  m_list = []
  return m_list


## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
