'''
  This tutorial session is targeted to illustrating one of the very
  generic function signature types that enables one to take in any
  type of variable-length arguments

  This includes the pros from both the previous two tutorial sections

>>> generic_function_type("non-keyworded", "arguments", "handling")
Argument# : non-keyworded
Argument# : arguments
Argument# : handling

>>> generic_function_type(name="Ethan Hunt", occupation="IMF Agent", latest="MI-6")
Key is name -> Value is Ethan Hunt
Key is occupation -> Value is IMF Agent
Key is latest -> Value is MI-6

>>> generic_function_type(1, 2, c=3, d=4, e=5)
Argument# : 1
Argument# : 2
Key is c -> Value is 3
Key is d -> Value is 4
Key is e -> Value is 5

  Q: Can you place a positional argument following a keyword argument ?
 
  Q: What do you think about argument packing ?
  
'''


# Start writing up the new code from here
# Start fixing up the broken code from here

def generic_function_type(args, kwargs):
  for arg in args:
    print("Argument# : {}".format(arg))
  for key, value in kwargs.items():
    print("Key is {} -> Value is {}".format(key, value))  

## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)