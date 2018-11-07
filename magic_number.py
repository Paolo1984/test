from random import *
import time 

x = randint(1,20)

def intro():
                print("Welcome to the slot machine!!")
                print("Enter your name:")
                a=str(input())
                print("Hey " + a + " let me introduce you to this simple game..")
                rules()

def rules():
                
                
                time.sleep(2)
                print("The system will extract a numer comprise between 1 and 20...")
                time.sleep(2)
                print("..you will have 3 attempt to find it and win...")
                time.sleep(2)
                print("...very easy!!...so, are you ready for the game???... please, enter yes or no..")
                b = str(input())
                if b == "yes" or b == "y":
                                print("GREAT!!")
                                time.sleep(2)
                                play()
                                
                else:
                                rules()

def play():
                print("Enter your lucky number!")
                y = int(input())
                while y != x:
                                if y > x:
                                                print("..mmm..too high, try again!")
                                                time.sleep(1)
                                                play2()
                                if y < x:
                                                print("...mmm..too low, try again!")
                                                time.sleep(1)
                                                play2()
                                else:
                                                print("CONGRATULATIONS!!!! YOU WIN!!!!!")
                                                doYouWannaPlayAgain()

def play2():
                print("Second attempt....let's go!")
                print("Enter your second lucky number!")
                y = int(input())
                while y != x:
                                if y > x:
                                                print("..mmm..too high, try again!")
                                                time.sleep(1)
                                                play3()

                                if y < x:
                                                print("...mmm..too low, try again!")
                                                time.sleep(1)
                                                play3()

                                else:
                                                print("CONGRATULATIONS!!!! YOU WIN!!!!!")
                                                doYouWannaPlayAgain()


def play3():
                print("Last attempt....let's go!")
                print("Enter your last lucky number!")
                y = int(input())

                if y == x:
                                print("CONGRATULATIONS!!!! YOU WIN!!!!!")
                                doYouWannaPlayAgain()

                else:
                                print("...emm... what can i say? you loose...sorry about that...")
                                doYouWannaPlayAgain()

def doYouWannaPlayAgain():
                print("Do you wanna play again?...yes for restart the game or no to end..")
                c = str(input())
                if c == "yes" or c == "y":
                                print("THIS IS A GREAT DAY TO BECAME A REAL PLAYER!!...LET'S START AGAIN!!")
                                rules()
                else:
                                print("Nice to meet you!! See you next time!")
                quit()
                                
                



                                

                                
                                

intro()
                                                
                
                                                      
