from objects.TicketCounter import TicketCounter
from objects.ConfigReader import ConfigReader
import os
import pytest
 
class TestTicketCounter():

    @pytest.fixture
    def my_filepath(self, tmpdir):
        return tmpdir.mkdir("sub").join("testCurrentTicketCount.txt")

    def test_createNewTicketCountFile(self, my_filepath):
        ticketCounter = TicketCounter(my_filepath)
        assert os.path.getsize(my_filepath) > 0

    def test_addOneTicketCounter(self, my_filepath):
        ticketCounter = TicketCounter(my_filepath)
        beforeCount = int(ticketCounter.readTicketCountFromFile())
        ticketCounter.addOneTicketCounter()
        afterCount = int(ticketCounter.readTicketCountFromFile())
        assert beforeCount + 1 == afterCount

    def test_readTicketCountFromFile(self, my_filepath):
        ticketCounter = TicketCounter(my_filepath)
        assert int(ticketCounter.readTicketCountFromFile()) >= 0



