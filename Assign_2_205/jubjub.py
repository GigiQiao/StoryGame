#storyline = ["0","1","2","3"] # this is the make choice to edit the story

import pickle
from time import sleep
import sys
import random # for user to make choice of each section


#Student name: Junya Qiao
#Student number: 5489877

# this is to read the story by input the name of the file to choose the story that want to read
# there will be list a list of choices
# by using the choice number as an input to make decisions
# when there is no other choice to make, the story end and the system exit
# when there is invalid input, then the system showing invalid input and let the user to make the decision again
choice = ""
temp = ""
start = ""
storydic = {}
choicelist = []
choices = []
# make a choice list that is the value of each key that let user to make choice to continue the story

#####----------load file -----start-----#####
def loadfile(name):
     with open('code/'+ name + '.pkl', 'r') as f:
          return pickle.load(f)
#####----------load file -----end-----#####

#####----------make the story begin -----start-----#####
def startstory(storydic):
     start = storydic.get("startingpoint")
     print("THIS IS THE STORY START: "+ str(start))
     return start
#####----------make the story begin -----end-----#####

#####----------make the story -----start-----#####
def storyline(choicelist,choice):
     choicelist = storydic.get(str(choice))
    # choicelist
     templength = len(choicelist[0])
     templist = choicelist[0]# choicelist = templist
     if(templength != 0):
          #tempc = choicelist[0]
          tempclength = len(choicelist[0])
          for i in range(tempclength):
               if(templist!="0"):
                    print("Choice "+ str(i+1)+" : "+ str(templist[i]))
          user_input = input("Please choocse the next stage of the story: ")
          if user_input == 1: # if equals to choice 1
               choice == 0
               if(templist[0]!="0"):
                    choice = templist[0]# move the key to the next stage
                    print("The Next Choice List")
               else:
                    user_input = input("Invalid choice")
                    
          if user_input == 2: # if equals to choice 2
               choice == 1
               if(templist[1]!="0"):
                    choice = templist[1]# move the key to the next stage

               else:
                    user_input = input("Invalid choice")
                    
          if user_input ==3: # if equals to choice 3
               choice == 2
               if(templist[2]!= "0"):
                    choice = templist[2]# mvoe the key to the next stage
                    print("The Next Choice List")

               else:
                    user_input = input("Invalid choice")
     testlist = storydic.get(str(choice))
     test = testlist[0]
     for k in range(3):
          if(test[1] and test[2] and test[0] =="0"):
               print("The end!")
               exit()
          else:
               storyline(choicelist, choice)
#####----------make the story -----end-----#####     

thename = raw_input("Please input the name of the story: ")
storydic = loadfile(thename)# get the dictionary of the story based on the story name
print(type(storydic))
choicelist = startstory(storydic)
choice = choicelist[0]
choicelist = storyline(choicelist,choice)

