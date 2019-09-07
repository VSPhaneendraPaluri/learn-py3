'''
  This tutorial section would be illustrating different aspects of using
  Python dictionary (a.k.a 'dict')

  The below automated test would demonstrate how to create nested dictionary
>>> nestedDictionary
{'Company-ABC': {\
'Anna': {'Age': 26},\
 'Fred': {'Age': 33}\
}\
}

  The below automated test should be used to fix the age for the employees
  to 28
>>> fixEmployeesAgeTo28()
{'Company-ABC': {\
'Anna': {'Age': 28},\
 'Fred': {'Age': 28}\
}\
}

  NOTE :  This tutorial shall also demonstrate usage of few features of a new
  Python module, namely, 'collections'

'''

# Import libraries here
import os
import collections


# Start writing up the new code from here
# Start fixing up the broken code from here
nestedDictionary = {
  'Company-ABC':
  {
    'Anna':{
      'Age': 26
    },
    'Fred':{
      'Age': 33
    }
  }
}

def updateAge(new_original, value_to_be_replaced):
  for key, value in new_original.items():
    if isinstance(value, collections.Mapping) and value:
      new_return = updateAge(new_original.get(key, {}), value_to_be_replaced)
      new_original[key] = new_return
    else:
      new_original[key] = value_to_be_replaced[key]
  return new_original

def fixEmployeesAgeTo28():
  modified_dict = updateAge(nestedDictionary, {'Age': 28})
  print(modified_dict)


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
