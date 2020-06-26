from objects.ConfigReader import ConfigReader
from objects.Model import TicketDF
from objects.ConfigReader import ConfigReader
from objects.TicketCounter import TicketCounter
import pandas as pd
from objects.Controller import Controller
from objects.view import view
import click

##program should work will all column names listed out in ticketAttributes.csv file
##make attachments only txt, jpg, png
##have attachments popup when viewing the ticket.
#make this work with click package, a cli tool
##create a while loop that always listens for input, could do some like b = back button, should be able to just type in ticket ID
##build a pipeline in bitbucket.
##write a commit hook and setup ec2 server listening
##add more functionality ot menu. can do two commands with one string: 3, PROT-23

@click.group()
@click.version_option(version='0.0.1', prog_name="Ticket Tracking CLI")
def main():
    """Ticket Tracking CLI"""
    pass
@main.command()
@click.argument('view', default='.')
def view(view):
    """View all current tickets assigned to user"""
    parser = ConfigReader()
    newView = view()
    controller = Controller(parser)
    print(controller.df[0])