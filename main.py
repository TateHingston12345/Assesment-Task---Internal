# Prerequisites - Variables and libraries required #
  # Libraries #
import csv
import time
import random
import os
  # Variables #
highscore = 0
# Functions - All functions for the program #
  # Randomise Function
def randomise(seq):
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)
  # Scores - Function to show previous scores #
def scores():
  if os.path.isfile("scores.csv"):
    with open('scores.csv', mode='r') as SCORES:
      csv_reader = csv.reader(SCORES, delimiter=',')
      for row in csv_reader:
        print("Name " + f'{row[0]}' + ", Score " + f'{row[1]}' + '.')
        time.sleep(0.1)
  # Learn - Function for listing the words and their meanings #
def learn():
  with open('Quiz.csv', mode='r') as QUIZCSV:
    csv_reader = csv.reader(QUIZCSV, delimiter=',')
    for row in csv_reader:
      if f'{row[0]}' == "Maori":
        print("Word Definitions:")
      else:
        print(f'{row[0]}')
        if f'{row[5]}' == "A":
          print(f'{row[1]}')
        elif f'{row[5]}' == "B":
          print(f'{row[2]}')
        elif f'{row[5]}' == "C":
          print(f'{row[3]}')
        elif f'{row[5]}' == "D":
          print(f'{row[4]}')
        time.sleep(0.25)
  # Test - Function for starting the test #
def test():
  with open('Quiz.csv', mode='r') as QUIZCSV:
    start = time.perf_counter()
    global highscore
    csv_reader = csv.reader(QUIZCSV, delimiter=',')
    correct = 0
    questions = 0
    for row in randomise(csv_reader):
      answered = 0
      if f'{row[0]}' == "Maori":
        print("Quiz Start:")
      else:
        print("What is the english definition of " + f'{row[0]}' + "?")
        while answered != 1:
          answer = input("A - " + f'{row[1]}' + ", B - " + f'{row[2]}' + ", C - " + f'{row[3]}' + ", D - " + f'{row[4]}' + ": ")
          if answer == "A" or answer == "B" or answer == "C" or answer == "D":
            if answer == f'{row[5]}':
              print("Correct, good job.")
              correct = correct + 1
              questions = questions + 1
              print("You currently have " + str(correct) + " out of " + str(questions) + ".")
              answered = 1
            else:
              print("Incorrect, the answer was " + f'{row[5]}' + ".")
              questions = questions + 1
              print("You currently have " + str(correct) + " out of " + str(questions) + ".")
              answered = 1
          else:
            print("Please enter a valid option.")
    end = time.perf_counter()
    score = int(((400-(end-start))*correct*10))
    if correct/questions >= 0.5 :
      print("You have passed the test, good job!")
      print("Your timed score was " + str(score) + ".")
      if score > highscore:
        print("That beats your previous highscore of " + str(highscore) + ".")
        highscore = score
        save = 0
        question = "Would you like to save your score: (Y/N) " 
        while save != 'N':
          save = str(input(question))
          if save == "Y":
            name = str(input("Please enter your name: "))
            with open('scores.csv', mode='a') as SCORES:
              csv_write = csv.writer(SCORES, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              csv_write.writerow([str(name), str(score)])
            save = "N"
          elif save == "N":
            break
          else:
            question = "Please enter a valid option."
      else:
        print("Your current highscore is " + str(highscore) + ".")
    else:
      print("You have failed, please go over definitions and try again.")
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