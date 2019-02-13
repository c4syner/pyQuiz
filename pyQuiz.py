import csv
import random
import sys
def clearwEnt():
	print("\n")
	trash = input("Enter to continue...")
	print("\n"*100)
def clear():
	print("\n"*100)
def runQuiz():
	clear()
	quizName = input("Quiz Name: ")
	case = input("Does case matter? (y/n): ")
	myFile = open(quizName, "w+")
	myQuiz = myFile.read()
	quizFormat= csv.reader(myQuiz)
	print(quizFormat[0])
	i = 0
	while(True):
		food = input()
	clearwEnt()
	lobby()
def buildQuiz():
	clear()
	quizName = input("Quiz Name: ")
	quizCount = int(input("Number of Questions: "))
	case = input("Does letter case matter? (y/n): ")
	myFile = open(quizName, "w+")
	i = 0
	while(True):
		i = i + 1
		
		que = input("Question " + str(i) + ": ")
		ans = input("Answer " + str(i) + ": ")
		if(case == "n" or case == "no" or case == "0"):
			ans = ans.lower()
		storage = que + "," + ans + "\n"
		myFile.write(storage)
		if(quizCount == i):
			break
	clearwEnt()
	lobby()
		

	
	
	

def lobby():
	clear()
	print("\tQuizWhizz")
	print("A Quiz Maker and Tester!")
	clearwEnt()
	print("1. Build a Quiz")
	print("2. Learn a Quiz")
	resp = int(input("Number: "))
	if(resp == 1):
		buildQuiz()
	elif(resp == 2):
		runQuiz()
	else:
		print("Invalid Option")
		exit(0)

lobby()	
	