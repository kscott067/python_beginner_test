import random

money = 100

#Write your game of chance functions here
def flip_coin(guess, bet):
  print("-------------")
  print("You choose to bet " + str(bet) + " dollars.")
  if bet <= 0:
    print("You must bet more than zero dollars")
    return 0
  if bet > money:
    print("You do not have enough money for this bet")
    return 0
  num = random.randint(1,2)
  if num == 1:
    print("The side is heads")
  elif num == 2:
    print("The side is tails")
  if ((guess == "Heads" or guess == "heads" or guess == "Heads!" or guess == "heads!") and num == 1) or ((guess == "Tails" or guess == "tails" or guess == "Tails!" or guess == "tails!") and num == 2):
    print("You win " + str(bet)+ " dollars!")
    return bet
  else:
    print("You lose " + str(bet)+ " dollars")
    return -bet
#enter your guess and bet here
money += flip_coin("heads", 100)
print("-----------------------")
print("You now have " + str(money) + " dollars.")
print("""


""")
def cho_han(guess, bet):
  print("Let's play a game of Cho-Han")
  print("-------------")
  print("You choose to bet " + str(bet) + " dollars.")
  if bet <= 0:
    print("You must bet more than zero dollars")
    return 0
  if bet > money:
    print("You do not have enough money for this bet")
    return 0
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  num = dice1+dice2
  print("The sum of the two dice is " + str(num)+".")
  if (num%2) == 0:
    print("The sum is even")
  elif (num%2) == 1:
    print("The sum is odd")
  if ((guess == "Even" or guess == "even" or guess == "Even!" or guess == "even!") and (num%2) == 0) or ((guess == "Odd" or guess == "odd" or guess == "Odd!" or guess == "odd!") and (num%2) == 1):
    print("You win " + str(bet)+ " dollars!")
    return bet
  else:
    print("You lose " + str(bet)+ " dollars")
    return -bet
#enter your cho-han guess and bet here
money += cho_han("odd", 100)
print("You now have " + str(money) + " dollars.")
print("""


""")
def pick_a_card(player1, player2, bet):
  print("Let's play a game of highest card wins")
  print("-------------")
  print(player1 + " and " + player2+ " choose to bet " + str(bet) + " dollars.")
  if bet <= 0:
    print("You must bet more than zero dollars")
    return 0
  if bet > money:
    print("You do not have enough money for this bet")
    return 0
  card1 = random.randint(1,10)
  card2 = random.randint(1,10)
  print(player1+"'s card is " + str(card1) + ".")
  print(player2+"'s card is " + str(card2) + ".")
  print(" ")
  if card1 > card2:
    print(player1 + " has the higher card. " + player1 + " wins "+ str(bet) + " dollars!")
    return bet
  if card1 < card2:
    print(player2 + " has the higher card. " + player2 + " wins "+ str(bet) + " dollars!")
    return -bet
  elif card1 == card2:
    print("Neither player has a higher card.")
    return 0
money += pick_a_card("Kameron", "Kelli", 75)
print("You now have " + str(money) + " dollars.")
print("""


""")
def roulette(guess, bet):
  print("Let's play a game of Roulette")
  print("-------------")
  print("You choose to bet " + str(bet) + " dollars.")
  if bet <= 0:
    print("You must bet more than zero dollars")
  if bet > money:
    print("You do not have enough money for this bet")
    return 0
  num = random.randint(0,37)
  #black = 2 or 4 or 6, 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 29 or 31 or 33 or 35
  #red = 1 or 3 or 5 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36
  print("You guessed " + str(guess) + " and the ball landed on "+str(num)+".")
  if guess == "Even" and (num%2) == 0 and num != 0:
    print("You guessed correctly and won "+ str(bet)+ " dollars!")
    return bet
  elif guess == "Odd" and (num%2) == 1 and num != 37:
    print("You guessed correctly and won "+ str(bet)+ " dollars!")
    return bet
  elif guess == num:
    print("You have dumb luck and guessed the exact number. Congrats you won "+ str(bet*35)+" dollars!")
    return bet * 35
  #elif guess == "Black" and num == black:
    #print("you won")
    #return bet
  #elif guess == "Red" and num == red:
    #print("you won")
    #return bet
  else:
    print("you lose")
    return -bet
money += roulette("Even", 100)
print("You now have " + str(money) + " dollars.")
 

#Call your game of chance functions here



#Call your game of chance functions here






#Call your game of chance functions here




















