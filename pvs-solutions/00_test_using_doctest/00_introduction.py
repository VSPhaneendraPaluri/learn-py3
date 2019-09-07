'''Welcome to the first introduction lab work on Python3 !

  Treat the contents within these commented section as both
    1. instruction steps to complete the lab tutorial
    2. expected output

  They would be very similar to what it would seem like some outputs
  from the Python command-line interpreters.
  
  Try to achieve the expected output by fixing up the broken code.

  NOTE : Fixing the code would be easier if one starts looking at the errors
  thrown by the interpreter from TOP to BOTTOM.

  This function write would let the users know how to return strings  
>>> main()
'Hello World !!'

>>> print_from_main()
This is printed from print_from_main() - Hello World !!

'''
  

# Start writing up the new code from here
# Start fixing up the broken code from here

def main():
  return 'Hello World !!'

def print_from_main():
  print("This is printed from print_from_main() - Hello World !!")

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
