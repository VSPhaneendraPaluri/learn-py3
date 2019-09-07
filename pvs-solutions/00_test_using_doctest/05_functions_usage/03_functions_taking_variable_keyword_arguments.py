'''
  This tutorial session is targeted to illustrating functions taking
  variable keyword arguments

  Using a variable keyword argument, the user can provide the
  name to the variable as you tend to pass in arguments to a function

  NOTE:  These keyword arguments can't be captured by the variable
         arguments capture idiom as illustrated in the
         '02_functions_taking_variable_arguments.py'

  The below automated test shall illustrate:
  - how to pass variable number of keyword arguments to a function.
  - These arguments are strictly keyworded type.
  - These are unordered as well

>>> function_taking_variable_keyword_arguments(name="Ethan Hunt", occupation="IMF Agent", latest="MI-6")
Key is name -> Value is Ethan Hunt
Key is occupation -> Value is IMF Agent
Key is latest -> Value is MI-6

>>> function_taking_variable_keyword_arguments(language="Python", conceiver="Guido van Rossum", year=1989)
Key is language -> Value is Python
Key is conceiver -> Value is Guido van Rossum
Key is year -> Value is 1989

  Q: Do you think that this function signature might be the most generic one ?
  A: Check the next tute - '04_generic_functions.py'

'''


# Start writing up the new code from here
# Start fixing up the broken code from here

def function_taking_variable_keyword_arguments(**kwargs):
  for key, value in kwargs.items():
    print("Key is {} -> Value is {}".format(key, value))  

## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)