from configparser import ConfigParser

config = ConfigParser()

config['settings']={
    'working_dir': 'C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/data'
}

config['files']={
    'tickets_csvpath': 'C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/data/tickets.csv',
    'ticket_count_path': 'C:/Users/jeffg/Desktop/ProgrammingProjects/ticket_tracking_system/data/currentTicketCount.txt'
}

config['initialization']={
    'ticket_attributes': ['Ticket ID','Subject','Project','Description','Priority','Comments','Attachments']
}

with open ('config/dev.ini', 'w') as f:
    config.write(f)