import os

class TicketCounter(): 
    
    def __init__(self, filepath):
        self.currentTicketCountFilePath = filepath
        if not (os.path.exists(filepath) and os.path.getsize(filepath) > 0):
            self.createNewTicketCountFile(filepath)
        self.setEnvCurrentTicketCount(self.readTicketCountFromFile())

    def readTicketCountFromFile(self):
        with open(self.currentTicketCountFilePath, 'r') as f:
            currentTicketCount = f.read()
        return currentTicketCount
    
    def writeTicketCountToFile(self):
        with open(self.currentTicketCountFilePath, 'w+') as f:
            f.write(os.getenv('Current_Ticket_Count'))

    def getEnvCurrentTicketCount(self):
        return os.getenv('Current_Ticket_Count')

    def setEnvCurrentTicketCount(self, ticketCount):
        os.environ['Current_Ticket_Count'] = ticketCount

    def addOneTicketCounter(self):
        count = int(os.getenv('Current_Ticket_Count'))
        count += 1
        self.setEnvCurrentTicketCount(str(count))
        self.writeTicketCountToFile()

    def createNewTicketCountFile(self, filepath):
        if not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
            except OSError: # Guard against race condition
                print("File error")
        with open(filepath, "w+") as file:
            file.write("1")

