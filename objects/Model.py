from ast import literal_eval
import pandas as pd
import os
import csv
import easygui as eg

class TicketDF():

###################################
#populate a df with ticket information stored in csv
###################################
    def getDFFromCSV(self, filepath):
        if self.doesFileExistAndNotEmpty(filepath):
            df = pd.read_csv(filepath, converters={'Comments':literal_eval, 'Attachments':literal_eval}) #, 'Attachments':literal_eval})
            df.set_index('Ticket ID', inplace=True)
            return df
        else:
            return pd.DataFrame()

###################################
#pass a list of columns that holds all the ticket attributes/columns
###################################
    def setTicketColumns(self, listOfColumns):
        self.ticketColumns = listOfColumns

###################################
#checks if filepath exists and size is greater than 0. Return true if fulfills both
###################################
    def doesFileExistAndNotEmpty(self, filepath):
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            return True
        else:
            return False

###################################
#passed a dataframe and dict, holding ticket data. Return df with data appended
###################################
    def addTicketToDF(self, df, data):
        newDF = pd.DataFrame (data, columns = self.ticketColumns)
        newDF.set_index('Ticket ID', inplace=True)
        df = df.append(newDF)
        return df
###################################
#passed a dataframe and file path. Save the df to the csv file.
###################################
    def saveDFToCSV(self, filepath, df):
        df.to_csv(filepath)

###################################
#Add new comment to ticket DF by locating the row by ticketID
#Then save the DF to csv
#Why does this not need a return value? https://stackoverflow.com/questions/38895768/python-pandas-dataframe-is-it-pass-by-value-or-pass-by-reference#:~:text=Return%20new%20object%20with%20labels,a%20new%20dataframe%20is%20created.&text=But%20as%20for%20all%20objects,to%20the%20function%20by%20reference.
#appending to a list does not mutate the df, creating a new object.
#So the object remains the same.
###################################
    def addCommentToTicketDF(self, df, ticketID, newComment):
        df.loc[ticketID]['Comments'].append(newComment)

###################################
#Add new attachment to ticket DF by locating the row by ticketID
#Then save the DF to csv
###################################
    def addAttachmentToTicketDF(self, df, ticketID, newAttachment):
        df.loc[ticketID]['Attachments'].append(newAttachment)