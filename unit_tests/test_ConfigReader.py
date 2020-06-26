from objects.ConfigReader import ConfigReader

def test_getTicketAttributes():
    parser = ConfigReader(False)
    assert type(parser.getTicketAttributes()) == type([])

def test_getTicketsCSVPath():
    parser = ConfigReader(False)
    assert parser.getWorkingDir() in parser.getTicketsCSVPath()

def test_getTicketCountPath():
    parser = ConfigReader(False)
    assert parser.getWorkingDir() in parser.getTicketCountPath()