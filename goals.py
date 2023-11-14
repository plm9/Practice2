import pandas as pd 
import time
import random

goals=pd.read_csv("goals.txt",delimiter=";",names=["Player","Country","time","dropper"])

goals.drop("dropper",inplace=True,axis=1)

def menu():
  print("*********************************************")
  print("*                                           *")
  print("*      2018 World Cup: Goals Analysis       *")
  print("*                                           *")
  print("*********************************************")
  print("")
  print("> Select an option:")
  print("       > A: Total number of goals scored by a given country")
  print("       > B: Total number of goals scored by a given player")
  print("       > C: List the name of all the players who scored for a given country")
  print("       > D: Total number of goals by all countries")
  print("       > E: Total number of goals scored during the first half (45 minutes)")
  print("       > F: Total number of goals scored during the second half (45 minutes to 90 minutes)")
  print("       > G: Total number of goals scored during extra time (after 90 minutes of play)")
  print("       > GAME: 2 teams game")
  print("       > X: Exit")
  print("")

""" A:Total number of goals scored by a given country """
def optionA():
    Countries=[]
    goalsperC={}
    for k in goals["Country"]:
        if k not in Countries:
            Countries.append(k)
            goalsperC[k]=1
        else:
            goalsperC[k]+=1
    userInput = input("> Enter country:").title()
    print("\n> " + userInput + " scored " + str(goalsperC[userInput]) + " goal(s) in the 2018 world cup.")
    

""" B:Total number of goals scored by a given player """
def optionB():
    Players=[]
    goalsperP={}
    for k in goals["Player"]:
        if k not in Players:
            Players.append(k)
            goalsperP[k]=1
        else:
            goalsperP[k]+=1
    userInput = input("> Enter country:").title()
    print("\n> " + userInput + " scored " + str(goalsperP[userInput]) + " goal(s) in the 2018 world cup.")

""" C:List the name of all the players who scored for a given country """
def optionC():
   Countries=[]
   PlayersperC={}
   for i,k in goals.iterrows():
        if k["Country"] not in Countries:
            Countries.append(k["Country"])
            PlayersperC[k["Country"]]=[k["Player"]]
        else:
            if k["Player"] not in PlayersperC[k["Country"]]:
                PlayersperC[k["Country"]].append(k["Player"])
   userInput = input("> Enter country:").title()
   print("\n> The player of" + userInput + " who scored are" + str(PlayersperC[userInput]) + " in the 2018 world cup.")

""" D: Total number of goals by all countries """
def optionD():
    Countries=[]
    goalsperC={}
    for k in goals["Country"]:
        if k not in Countries:
            Countries.append(k)
            goalsperC[k]=1
        else:
            goalsperC[k]+=1
    
    print("\n> In the 2018 wotld cup the number of goals by all counties were:")
    
    for c,g in zip(goalsperC.keys(),goalsperC.values()):
       print("\n>"+c+" scorer "+str(g)+" goals")
    print("With a number of total goals "+str(sum(goalsperC.values())))   

""" E: Total number of goals scored during the first half (45 minutes) """    
def optionE():
   goals1st=0
   for k in goals["time"]:
      if k<=45: goals1st+=1
   print("\n> The number of goals that were achieved in the first half were "+str(goals1st))   

""" F: Total number of goals scored during the second half (45 minutes to 90 minutes) """    
def optionF():
   goals1st=0
   for k in goals["time"]:
      if k>45 and k<=90: goals1st+=1
   print("\n> The number of goals that were achieved in the second half were "+str(goals1st))   

""" G: Total number of goals scored during the extra time (after 90 minutes of play) """    
def optionG():
   goals1st=0
   for k in goals["time"]:
      if k>90: goals1st+=1
   print("\n> The number of goals that were achieved in the extra time were "+str(goals1st))   

""" GAME:  2 teams game) """    
def optionGAME():
    Countries=[]
    goalsperC={}
    for k in goals["Country"]:
        if k not in Countries:
            Countries.append(k)
            goalsperC[k]=1
        else:
            goalsperC[k]+=1

    rndCntr1=random.choice(Countries)
    rndCntr2=random.choice(Countries)
    while rndCntr1==rndCntr2:
       rndCntr2=random.choice(Countries)

    if goalsperC[rndCntr1]>goalsperC[rndCntr2]:
       moreGoals=rndCntr1
       lessG=rndCntr2
    elif goalsperC[rndCntr1]<goalsperC[rndCntr2]:
       moreGoals=rndCntr2
       lessG=rndCntr1
    else:
       moreGoals=None
       lessG=None
    
    userInput=input("\n> Between "+rndCntr1+" and "+rndCntr2+" which team scored more goals on the 2018 world cup? ")
    
    if moreGoals:
       if userInput==moreGoals:
          print("\n> Congrats!"+userInput+" scored "+str(goalsperC[userInput])+" and "+lessG+" scored "+str(goalsperC[lessG]))
       else:
          print("\n> Unfortunately you lost!"+userInput+" scored "+str(goalsperC[userInput])+" and "+moreGoals+" scored "+str(goalsperC[moreGoals]))    
    else:
       if userChoice=="equal":
          print("\n> Congrats!"+userInput+" scored "+str(goalsperC[userInput])+" and "+lessG+" scored "+str(goalsperC[lessG]))
       else:
          print("\n> Unfortunately you lost!"+userInput+" scored "+str(goalsperC[userInput])+" and "+moreGoals+" scored "+str(goalsperC[moreGoals])+" meaning the scored the same amount of goals!")


userChoice=""
while userChoice!="X":
  menu()
  userChoice = input("> Select an option from the menu (A to G) or X to exit:").upper()
  if userChoice=="A":
    optionA()
  elif userChoice=="B":
    optionB()
  elif userChoice=="C":
    optionC()
  elif userChoice=="D":
    optionD()
  elif userChoice=="E":
    optionE()  
  elif userChoice=="F":
    optionF()  
  elif userChoice=="G":
    optionG()  
  elif userChoice=="GAME":
    optionGAME()  

  time.sleep(2)
  print("\n\n\n")
print("Good bye!") 


