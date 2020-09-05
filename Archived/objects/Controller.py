import os
from objects.Model import TicketDF
from objects.TicketCounter import TicketCounter
import pandas as pd
from objects.view import view
import re
import easygui as eg

class Controller():

    def __init__(self, configParser):
        self.parser = configParser
        self.view = view()
        self.ticketCounter = TicketCounter(self.parser.getTicketCountPath())
        self.ticketDF = TicketDF()
        self.df = self.ticketDF.getDFFromCSV(self.parser.getTicketsCSVPath())
        self.ticketDF.setTicketColumns(self.parser.getTicketAttributes())

###################################
#Called when user wants to create a ticket. Grab user input and store as dict. Add to ticket dict to df and add plus one to
#ticketcounter in text file. Ask if user wants to make an attachment. Print created ticket out to the user.
###################################
    def newTicket(self):
        data = self.view.getTicketInputAsDict()
        self.df = self.ticketDF.addTicketToDF(self.df, data)
        self.ticketCounter.addOneTicketCounter()
        if self.view.wouldYouLikeAttachment():
            newAttachmentPath = self.view.getAttachmentPath()
            self.ticketDF.addAttachmentToTicketDF(self.df, data['Ticket ID'], newAttachmentPath)
        print(self.df.loc[data['Ticket ID']])
        self.ticketDF.saveDFToCSV(self.parser.getTicketsCSVPath(), self.df)

###################################
#called when user selects to view tickets.
###################################
    def viewTickets(self):
        self.view.displayTickets(self.df)

###################################
#Called when user wants to select ticket. Select ticket by ID, entered by user.
#Ask if user wants to comment or attach file. Prints ticket after creation.
###################################
    def selectTicket(self):
        ##needs to have an options ability: should be able to make a comment, change the status
        if not self.df.empty:
            ticketID = input("Please enter the ticket ID: ")
            print(self.df.loc[ticketID])
            if len(self.df.loc[ticketID]['Attachments']) > 0:
                print("Please look at the pop up window for attachments.")
                for x in self.df.loc[ticketID]['Attachments']:
                    eg.buttonbox(x,image=x,choices=[])
            if self.view.wouldYouLikeToComment():
                newComment = self.view.getNewCommentFromUser(ticketID)
                self.ticketDF.addCommentToTicketDF(self.df, ticketID, newComment)
                self.ticketDF.saveDFToCSV(self.parser.getTicketsCSVPath(), self.df)
            if self.view.wouldYouLikeAttachment():
                newAttachmentPath = self.view.getAttachmentPath()
                self.ticketDF.addAttachmentToTicketDF(self.df, ticketID, newAttachmentPath)
                self.ticketDF.saveDFToCSV(self.parser.getTicketsCSVPath(), self.df)
        else:
            print("The ticket queue is currently empty.")

###################################
#Returns True if is invalid option. Checks the userChoice and calls functions accordingly.
###################################
    def manageInput(self, userChoice):
        if bool(re.match(r'[0-3]', userChoice)):
            if(int(userChoice) == 1):
                self.newTicket()
                return False
            elif (int(userChoice)==2):
                self.viewTickets()
                return False
            elif (int(userChoice)==3):
                self.selectTicket()
                return False
        else:
            print("Please enter a valid option.")
            return True