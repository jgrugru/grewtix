Gru Tick
======
 Introduction
 ----------------
Gru Tick is a ticket tracking system built through Django (v3.0.6). Through Gru Ticket, you can create tickets for work/projects/teams and assign them as needed. Gru Tick is in the beginning stages of development so many features are coming soon. You can view progress at the bottom of this README.

 Requirements
 ----------------
 - Django==3.0.6
 - django-widget-tweaks==1.4.8

 How to Get Started
 ----------------
 * Install virtualenv and create virtual environment on local machine ```pip install virtualenv```
 * 
Navigate to the *ttsystem* (Ticket Tracking System) dir and enter the following commands: 
 * *python manage.py makemigrations*
 * *python manage.py migrate*
 * *python manage.py runserver*

 * Installation
 * Configuration
 * Troubleshooting
 * FAQ
 * Maintainers

Reason for development
----------------------
This project started as a way to learn Python, but has turned into an ongoing project with the hopes of being a useful ticketing system. When I began this project, I had only worked with Youtrack, JetBrains ticketing system. You may be able to notice some similarities. 

Features to add
---------------
 * <strike>migrate to Django framework.</strike>
 * <strike>add owner field in ticket model</strike>
 * <strike>add navbar</strike>
 * <strike>ticket's priority field should be limited to low, medium, high, critical.</strike> Remove priority model
 * <strike>default of owner/assignee should be unassigned/null</strike>
 * <strike>create ticket edit page</strike>
 * <strike>use generic views</strike>
 * <strike>modify ticket create form page for easier use (assignee on the right side, creator field automatically added)</strike>
 * setup unit tests
 * Create own user model and integrate into other models
 * add comment functionality
 * add attachment functionality
 * view all tickets by project (make it the homepage dashboard)

 * Create a simple reports page (total finished tickets, tickets finished by user)
 * Create admin page to modify profile settings
 * setup two different types of user permissions: admin and user
 * add reviewers to tickets
 * add labels field to tickets
 * dynamically create title of page for new ticket EX: PROD-12

Long term goals
------------------------
 * Create teams/groups to view tickets inside teams/groups
 * Create customizable dashboard
 * Add api for dynamic ticket creation
 * Add api for list of tickets sorted by user/team/project/etc.
 * Add time tracking for in progress tickets or manual entry of time

 