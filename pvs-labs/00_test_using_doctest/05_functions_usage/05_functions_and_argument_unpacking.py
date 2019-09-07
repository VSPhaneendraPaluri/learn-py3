'''
  This tutorial section is targetted to demonstrate the use of arguments unpacking

>>> function_taking_exact_number_of_list_elements(1, 2, 3, 4, 5)
Number of elements are : 5
Element# 1: 1
Element# 2: 2
Element# 3: 3
Element# 4: 4
Element# 5: 5

  The below automated tests helps one in understanding the arguments unpacking

>>> list1
[5, 10, 15, 20, 25]

  NOTE :  This time around, the python session needs to be FIXED HERE !
>>> function_taking_exact_number_of_list_elements(list1)
Number of elements are : 5
Element# 1: 5
Element# 2: 10
Element# 3: 15
Element# 4: 20
Element# 5: 25


'''

# Start writing up the new code from here
# Start fixing up the broken code from here

def function_taking_exact_number_of_list_elements(first, second, third, fourth, fifth):
  print("Number of elements are : 5")
  print("Element# 1: {}".format(first))
  print("Element# 2: {}".format(second))
  print("Element# 3: {}".format(third))
  print("Element# 4: {}".format(fourth))
  print("Element# 5: {}".format(fifth))

list1 = []


## DO NOT modify anything below this !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
