# Prerequisites - Variables and libraries required #
  # Libraries #
import csv
import time
# Functions - All functions for the program #
  # Test - Function for starting the test #
def test():
  print("pog")
  # Learn - Function for listing the words and their meanings #
def learn():
  print("pog")
  # Scores - Function to show previous scores #
def scores():
  print("pog")
  # Menu - Function to select what to do #
def menu():
  option = 256
  question = "What would you like to do?" 
  while option != 0:
    print(question)
    question = "What would you like to do?"
    option = input("0 - quit, 1 - test, 2 - learn, 3 - view scores: ")
    if option == "1":
      test()
    elif option == "2":
      learn()
    elif option == "3":
      scores()
    elif option == "0":
      break
    else:
      question = "Please enter a valid option."
# Program - Runs the program #
  # Runs Menu Function #
menu()
