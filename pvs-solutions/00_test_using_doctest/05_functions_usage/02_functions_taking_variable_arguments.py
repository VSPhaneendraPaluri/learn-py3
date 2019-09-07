'''
  This tutorial would help the users understand the right syntax for
  passing variable arguments to a functions in Python

  The below automated test shall illustrate:
  - how to pass variable number of arguments to a function.
  - These arguments are strictly non-keyworded type.
  - These are strongly ordered as well

>>> function_taking_variable_arguments('one', 'two', 'three', 'four', 'five')
['one', 'two', 'three', 'four', 'five']

>>> function_taking_variable_arguments('a', 'b', ['c', 'd', 'e'])
['a', 'b', ['c', 'd', 'e']]

>>> function_taking_variable_arguments(1, 2, 3, 4, 5, 6)
[1, 2, 3, 4, 5, 6]

  Can you guys guess what could be the corner case where this proposed
  solution might hit a roadblock ?
  Check out the next tute - '03_function_taking_keyword_arguments.py'


'''


# Start writing up the new code from here
# Start fixing up the broken code from here

# Function accepting any number of arguments and returning
# the arguments list
def function_taking_variable_arguments(*xargs):
  argList = []
  for argument in xargs:
    argList.append(argument)
  return argList


## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
