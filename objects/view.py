import pandas as pd
import os
import easygui as eg
from datetime import datetime


class view():

###################################
#Display the options for the user.
###################################
    def displayMenu(self):
        print("------------------------------")
        print("What would you like to do?")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Select Ticket")
        print("------------------------------")

###################################
#takes df as argument and prints it out in certain format
###################################
    def displayTickets(self, df):
        if df.empty:
            print("The ticket queue is currently empty.")
        else:
            print("--------------------------------")
            print(df)
            # with pd.option_context('display.colheader_justify','left', 'display.max_colwidth', 10):
            #     print(df[['Subject', 'Description']])

###################################
#Gets user input needed to create a ticket. Returns ticket data in dictionary.
###################################
    def getTicketInputAsDict(self):
        subject = input('Enter Subject of Ticket: ')
        project = input('Enter Project Affected by Issue: ')
        description = input("Enter brief description of issue: ")
        priority = input("Enter the priority - Low, Medium, High, Critical: ")
        ticketID = "PROT-" + os.getenv('Current_Ticket_Count')
        status="Waiting on Support"
        creationDate=datetime.now()
        ##this needs to be setup in a for loop with ticketAttributes list
        data = {
            'Ticket ID': ticketID,
            'Subject': subject,
            'Project': project,
            'Description': description,
            'Priority': priority,
            'Comments': [[]],
            'Attachments': [[]],
            'Status': status,
            'Creation Date':creationDate,
            'Creator': os.getlogin()
        }
        return data

###################################
#Returns true or false, corresponding to y or n userinput
###################################
    def wouldYouLikeToComment(self):
        userDecision = input("Would you like to comment on this ticket? Y or N? ")
        return self.isItYes(userDecision)

###################################
#Returns true or false, corresponding to y or n userinput
###################################
    def wouldYouLikeAttachment(self):
        userDecision = input("Would you like to make an attachment? Y or N? ")
        return self.isItYes(userDecision)

###################################
#opens popup window for attachments. Returns file path.
###################################
    def getAttachmentPath(self):
        print("Please use the pop up window")
        return eg.fileopenbox(default='\*.gif', filetypes=['.jpg','.png','.gif'])

###################################
#Asks user to comment and returns input.
###################################
    def getNewCommentFromUser(self, ticketID):
        return input("Please enter your comment: ")

###################################
#returns True if charinput is y or Y, else return False
###################################
    def isItYes(self, charInput):
        if charInput == "Y" or charInput == 'y':
            return True
        else:
            return False