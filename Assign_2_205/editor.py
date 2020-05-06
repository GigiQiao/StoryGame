import curses
import pickle #Serialization module for python
#import random; # for making the choices of the storyline
#import time; # this is for the paulse time for the story telling.
import sys# this is to get the system input from the keyboard

#Student name: Junya Qiao
#Student number: 5489877

storydic = {} # initalize the story
sublist = [] # adding element to the subsections
hold = ""
num = 3 # the max of next stage is 3
sublist = []
temp= {}
#The editor is to edit a story, it start by edit a beginning of a story with three choices.
# The story will always have 3 choice in each section
# If this is the end of the story, then add "0"  or ""(empty string)as the section end
# otherwise, there should have make this to a key that direct to other section
# the story can be halted by edit "halt();" into the screen to finish editing (no matter the story stops or not)
# or it will stop when the story is full and have no keys to direct other sections
# the story is saved by using pickle to a binary file

var = raw_input("please input the start of the story: ")
print("story begin: "+ str(var))
#storydic.update({"story1": var})
storydic.update({"startingpoint":[var]})
storydic.update({var : []})# beginning line of the story
hold = var

#####----------writeSubsections -----start-----#####               
def writeSub(num):
        del sublist[:]
        for i in range(num):
                var = raw_input("add subsection as(" +str(i+1)+ ")" )# ask for new subsection
                print("subsection"+ str(i+1)+ str(var))
                sublist.append(var)
                print("sublist   "+  str(sublist))
                storydic.update({var:[]})
                print(storydic)
        storydic[hold].append(list(sublist))
        return sublist


#####----------writeSubsections -----end-----##### 

#####----------append inside the subsection (recursion part) -----start-----#####
def addDictionary():
        for sub in list(storydic.keys()):
                if (bool (storydic[sub]) == False):
                        #del sublist[:]
                        print(sub)
                        sublist = getlist()
                        print("this is the subsection: ~~~")
                        print(sub)
                        storydic[sub].append(list(sublist))
        print(storydic)
        return storydic       
#####----------append inside the subsection -----end-----#####

#####----------check the key -----start-----#####
# check the dictionary to see if there is already the end of story
#and do not need key to continue the story
def checkdic(storydic):
        for key in list(storydic.keys()):
                if(key == "0" or key == ""):
                        list(storydic.pop(key))
                        print ("HOHOHO LoOK at ME")
                        print(storydic)
        return storydic

#####----------check the key -----end-----#####

#####----------get a list for the sub section -----start-----#####
def getlist():
        del sublist[:]
        for i in range(num):
                element = raw_input("get subsection: ("+ str(i+1)+ ")")
                sublist.append(element)
                storydic.update({element:[]})
        return sublist                     
#####----------get a list for the sub section -----end-----#####

#####----------get a list for the save the dictionary as a file -----start-----#####
def savefile(name):
        with open('code/' + name + '.pkl', 'w') as f:
                pickle.dump(storydic, f, pickle.HIGHEST_PROTOCOL)
        

#####----------get a list for the save the dictionary as a file -----end-----#####
   
writeSub(num)
checkdic(storydic)
#if value in list(storydic.values() = []):## when there is still empty value for the key, then still running the loop
        ##otherwise, it is the end and generate the txt or binary file for the loop
for i in range(30): # maximum of 30 pages
        addDictionary()
        checkdic(storydic)
thename = raw_input("please input the name of the story ")
savefile(thename)# save to a binary file
