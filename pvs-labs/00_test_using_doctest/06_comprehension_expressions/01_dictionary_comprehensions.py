'''
  The following session illustrates the users the power of Python
  in the form of comprehension expressions

  NOTE :
    Python2 introduced LIST comprehensions for the first time.
    Python3 introduced DICT and SET comprehensions

  Python language constructs have provided an efficient way to create
  nested lists, dicts or sets, or loop(s), etc.
  These expressions are a better replica of the mathematical expressions
  that usually mathematicians would generally use in order to generate
  lists, sequences, or some number patterns based on a logic.

>>> userDict
{\
'one': 1, \
'two': 2, \
'three': 3, \
'four': 4\
}

  The below automated test illustrates iterating over a dictionary using comprehensions
  and modify the values of the dict keys
>>> newUserDictValues
{\
'one': 2, \
'two': 4, \
'three': 6, \
'four': 8\
}

  The below automated test illustrates iterating over a dictionary using comprehensions
  and modify the dict keys themselves
>>> newUserDictKeys
{\
'oneone': 2, \
'twotwo': 4, \
'threethree': 6, \
'fourfour': 8\
}

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

userDict = {}

newUserDictValues = {}

newUserDictKeys = {}

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
