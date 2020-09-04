from configparser import ConfigParser, ExtendedInterpolation
from ast import literal_eval

class ConfigReader():

    def __init__(self, isNotUnitTest=True):
        self.parser = ConfigParser(interpolation=ExtendedInterpolation())
        if isNotUnitTest:
            self.parser.read('ticket_tracking_system/config/dev.ini')
        else:
            self.parser.read('config/test.ini')

    def getTicketAttributes(self):
        return literal_eval(self.parser.get('initialization', 'ticket_attributes'))

    def getTicketsCSVPath(self):
        return self.parser.get('files', 'tickets_csvpath')

    def getTicketCountPath(self):
        return self.parser.get('files', 'ticket_count_path')

    def getWorkingDir(self):
        return self.parser.get('settings','working_dir')