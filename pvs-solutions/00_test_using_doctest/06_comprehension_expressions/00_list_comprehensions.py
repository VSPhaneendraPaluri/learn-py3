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

  The below automated test illustrates generating a sequence (list) of numbers
  using comprehensions

>>> generateWholeNumbersTill11
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

  NOTE: For the below expression, consider the input string to be - 'Python'
  Output should consists of all characters in a list
>>> spellOutCharactersInAString
['P', 'y', 't', 'h', 'o', 'n']

  The below test demonstrates the use of expression
>>> generateFirstFiveCubes
[1, 8, 27, 64, 125]

  The below automated test illustrates how the sequences could be generated
  and used further

  // Mathematical equivalent
  N = { n : n such that n belongs to odd numbers group [1..5]}
  S = { s^2 : s such that s is square of every n in N}
>>> S
[1, 4, 9, 16, 25]

  The below automated test demonstrates use of conditional expressions inorder to
  generate a list of odd numbers from the above generated sequence S 
>>> locateOddInS
[1, 9, 25]

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

generateWholeNumbersTill11 = [num for num in range(0, 12)]

spellOutCharactersInAString = [char for char in 'Python']

generateFirstFiveCubes = [num**3 for num in range(1,6)]

N = [ n for n in range(1, 6) ]
S = [ s**2 for s in N ]

locateOddInS = [ n for n in S if (n % 2 != 0) ]

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
