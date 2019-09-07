'''
  The following tutorial shall get the user to kick-start parsing
  command-line arguments using 'argparse' module

  The below automated test shall demonstrate how input arguments are parsed

  NOTE: Also note the the way default values are provided to the command-line
  arguments

>>> compute_total_amount(['--currencyType', 'INR'])
Total Amount entered is : INR 2880

>>> compute_total_amount(['--currencyType', 'INR', '--numberOfTwoThousands', '2'])
Total Amount entered is : INR 4880

>>> compute_total_amount(['--currencyType', 'INR', '--numberOfTens', '2'])
Total Amount entered is : INR 2890

'''

import argparse

parser = argparse.ArgumentParser(prog="CurrencyCalculator")

parser.add_argument("--currencyType", help="Input the currency type - INR or USD", type=str)
parser.add_argument("--numberOfTwoThousands", help="Enter the number of Two Thousand rupee notes", type=int, default=1)
parser.add_argument("--numberOfFiveHundreds", help="Enter the number of Five Hundred rupee notes", type=int, default=1)
parser.add_argument("--numberOfTwoHundreds", help="Enter the number of Two Hundred rupee notes", type=int, default=1)
parser.add_argument("--numberOfOneHundreds", help="Enter the number of One Hundred rupee notes", type=int, default=1)
parser.add_argument("--numberOfFifties", help="Enter the number of Fifty rupee notes", type=int, default=1)
parser.add_argument("--numberOfTwenties", help="Enter the number of Twenty rupee notes", type=int, default=1)
parser.add_argument("--numberOfTens", help="Enter the number of Ten rupee notes", type=int, default=1)


def compute_total_amount(inputArguments):
  arguments = parser.parse_args(args=inputArguments)
  totalAmount = (arguments.numberOfTwoThousands * 2000) +\
    (arguments.numberOfFiveHundreds * 500) +\
    (arguments.numberOfTwoHundreds * 200) +\
    (arguments.numberOfOneHundreds * 100) +\
    (arguments.numberOfFifties * 50) +\
    (arguments.numberOfTwenties * 20) +\
    (arguments.numberOfTens * 10)
  print("Total Amount entered is : {} {}".format(arguments.currencyType, totalAmount))


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
