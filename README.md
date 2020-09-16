Ticket Based Tracking System
================================

Reason for development
----------------------
This is the first project I have developed in Python. It started as a way to learn and grow my skills with Python.

How to Run
----------
Navigate to the *ttsystem* (Ticket Tracking System) dir and enter the following commands: 
 * *python manage.py makemigrations*
 * *python manage.py migrate*
 * *python manage.py runserver*

Features to add
---------------
 * <strike>migrate to Django framework.</strike>
 * <strike>add owner field in ticket model</strike>
 * <strike>add navbar</strike>
 * setup unit tests
 * create ticket edit page
 * use generic views
 * view all tickets by project (make it the homepage dashboard)
 * modify ticket create form page for easier use (assignee on the right side, creator field automatically added)
 * Create a simple reports page (total finished tickets, tickets finished by user)
 * Create admin page to modify profile settings
 * Create own user model and integrate into other models
 * setup two different types of user permissions: admin and user

Long term goals
------------------------
 * Create teams/groups to view tickets inside teams/groups
 * Create customizable dashboard
 * Add api for dynamic ticket creation
 * Add api for list of tickets sorted by user/team/project/etc.
 * Add time tracking for in progress tickets or manual entry of time

 