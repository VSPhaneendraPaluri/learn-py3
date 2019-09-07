'''

  This tutorial section would be illustrating different aspects of using
  Python dictionary (a.k.a 'dict')

  Dictionary - is a set of Key-Value Pair (KVP) or Name-Value Pair (NVP)

  How does one define an empty dict ?
>>> dict1
{}

  The below automated test creates a dictionary with integer as the Key component
>>> dict2
{1: 'One', 2: 'Two', 3: 'Three'}

  The below automated test creates a dictionary object with mixed keys
>>> dict3
{1: 'One', 'T-W-O': ['Two', 2]}

  The below automated test lets you pick the value using the key
>>> valueOfKey2OfDict2
'Two'

  The below automated test would demonstrate how to create nested dictionary
>>> nestedDictionary
{'Company-ABC': {\
'Anna': {'Age': 26},\
 'Fred': {'Age': 33}\
}\
}

'''

# Import libraries here
import os


# Start writing up the new code from here
# Start fixing up the broken code from here
dict1 = None
dict2 = {}
dict3 = {}
valueOfKey2OfDict2 = ''
nestedDictionary = {}


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
