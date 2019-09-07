'''
  This file lists tests for automated testing of inputs provided on command line.

  This automated test is a positive test that verifies and validates that the input command-line
  arguments are correct
>>> parse_command_line_arguments(['--help', '--inputFileName', 'input.txt', '--outputFileName', 'output.txt'])
Help Information requested
InputFileName : input.txt
OutputFileName : output.txt

>>> parse_command_line_arguments(['--inputFileName', 'input.txt', '--outputFileName', 'output.txt'])
InputFileName : input.txt
OutputFileName : output.txt

  This automated test is a negative test that verifies and validates that the input command-line
  arguments are incorrect and throws out a standard error
>>> parse_command_line_arguments(['--inputFileName', 'input.txt', '--newArgumentOption', 'newValue'])
option --newArgumentOption not recognized

'''

## Import libraries here - uncomment the below line
import sys
import getopt

# Start writing up the new code from here
# Start fixing up the broken code from here

def print_help():
  print("Help Information requested")

def print_input_details(argument):
  print("InputFileName :", argument)

def print_output_details(argument):
  print("OutputFileName :", argument)

def handle_command_line_arguments(opts, args):
  verbose = False
  for option, argument in opts:
    if option in ('-v'):
      verbose = True
    elif option in ("-h", "--help"):
      print_help()
    elif option in ("-i", "--inputFileName"):
      print_input_details(argument)
    elif option in ("-o", "--outputFileName"):
      print_output_details(argument)

def parse_command_line_arguments(arguments):
  try:
    opts, args = getopt.getopt(arguments, "io:hv", ["help","inputFileName=","outputFileName="])
  except getopt.GetoptError as error:
    print(str(error))
    return
  handle_command_line_arguments(opts, args)


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  parse_command_line_arguments(sys.argv[1:])
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
