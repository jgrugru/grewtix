from objects.Model import TicketDF
from objects.ConfigReader import ConfigReader
import os
import random
import pandas as pd
import pytest

class TestTicketDF():

    @pytest.fixture(scope="module")
    def my_parser(self):
        return ConfigReader(False)

    @pytest.fixture(scope="module")
    def my_ticketDF(self):
        return TicketDF()

    def test_getDFFromCSV(self, tmpdir, my_ticketDF):
        df = my_ticketDF.getDFFromCSV(tmpdir.mkdir("sub").join("testTicketsDF.csv"))
        assert isinstance(df, pd.DataFrame)

    def test_setTicketColumns(self, my_parser, my_ticketDF):
        my_ticketDF.setTicketColumns(my_parser.getTicketAttributes())
        assert my_ticketDF.ticketColumns == ['Ticket ID', 'Subject', 'Project', 'Description', 'Priority', 'Comments', 'Attachments',\
            'Status', 'Creation Date', 'Creator']

    def test_doesFileExistAndNotEmpty(self, my_ticketDF):
        assert my_ticketDF.doesFileExistAndNotEmpty('C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/main.py')

    def test_addTicketToDF(self, my_ticketDF):
        df = pd.DataFrame()
        data = self.mockTicketData(my_ticketDF.ticketColumns)        
        df = my_ticketDF.addTicketToDF(df, data)
        assert len(df.index.values) == 1

    def test_saveDFToCSV(self, tmpdir, my_ticketDF):
        x = tmpdir.mkdir("sub").join("testTicketsDF.csv")
        my_ticketDF.saveDFToCSV(x, pd.DataFrame.from_dict(self.mockTicketData(my_ticketDF.ticketColumns)))
        sizeAfter = os.path.getsize(x)
        assert sizeAfter > 5

    def test_addCommentToTicketDF(self, my_ticketDF):
        data = self.mockTicketData(my_ticketDF.ticketColumns)
        df = pd.DataFrame.from_dict(data)
        df.set_index('Ticket ID', inplace=True)
        my_ticketDF.addCommentToTicketDF(df, data['Ticket ID'], "This is a unit test")
        assert df.loc[data['Ticket ID']]['Comments'][1] == "This is a unit test"

    def test_addAttachmentToTicketDF(self, my_ticketDF):
        data = self.mockTicketData(my_ticketDF.ticketColumns)
        df = pd.DataFrame.from_dict(data)
        df.set_index('Ticket ID', inplace=True)
        my_ticketDF.addAttachmentToTicketDF(df, data['Ticket ID'], "C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/data/tickets.csv")
        assert df.loc[data['Ticket ID']]['Attachments'][1] == "C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/data/tickets.csv"

    def mockTicketData(self, ticketColumns):
        data = {'Ticket ID':'PROT-5000'}
        for x in ticketColumns:
            if not x == 'Ticket ID':
                if x == 'Comments' or x == 'Attachments':
                    data[x]=[['unit test']]
                else:
                    data[x] = 'unit test'
        return data