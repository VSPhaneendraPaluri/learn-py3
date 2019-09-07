'''

  This tutorial would help the users understand the right syntax that
  are possible with functions usage in Python

  This automated test shall enable the function to take in normal arguments
  along with arguments having default parameters
>>> add_all_user_input_numbers(1, 2, 3, 4)
10

>>> add_all_user_input_numbers(1, 2)
33

>>> add_all_user_input_numbers(1, 2, z4 = 30)
43

>>> add_all_user_input_numbers(1, 2, z3 = 30, z4 = 30)
63

>>> add_all_user_input_numbers(1, 2, z4 = 30, z3 = 40)
73

'''

# Import Python modules
import sys


# Start writing up the new code from here
# Start fixing up the broken code from here

def add_all_user_input_numbers(z1, z2, z3 = 10, z4 = 20):
  return (z1 + z2 + z3 + z4)


## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
