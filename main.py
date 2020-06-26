from objects.ConfigReader import ConfigReader
from objects.Model import TicketDF
from objects.ConfigReader import ConfigReader
from objects.TicketCounter import TicketCounter
import pandas as pd
from objects.Controller import Controller
from objects.view import view

##program should work will all column names listed out in ticketAttributes.csv file
##make attachments only txt, jpg, png
##have attachments popup when viewing the ticket.
#make this work with click package, a cli tool
##create a while loop that always listens for input, could do some like b = back button, should be able to just type in ticket ID
##build a pipeline in bitbucket.
##write a commit hook and setup ec2 server listening
##add more functionality ot menu. can do two commands with one string: 3, PROT-23
parser = ConfigReader()
myView = view()
myController = Controller(parser)
userChoice = 100
while(int(userChoice) != 0):
    myView.displayMenu()
    userChoice = input("Please enter the number: ")
    ifIsInvalidOption = myController.manageInput(userChoice)
    if ifIsInvalidOption:
        userChoice = 100 #set to arbitrary number, so that if userchoice is a str it will not fail the int(userChoice) != 0
