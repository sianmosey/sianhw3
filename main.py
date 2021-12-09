from random import randint

player = input("Choose rock, paper or scissors: ")

print("player chose: " + player)

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0,2)]

print("computer chose: " + computer)