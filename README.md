__Grewtix__
============
    
 Introduction
 ----------------
Grewtix is a ticket tracking system built through the Python (3.8.5) framework Django (3.0.6). Through Grewtix, you can create tickets for work/projects/teams and assign them as needed. Grewtix is in the beginning stages of development so many features are coming soon. You can view progress at the bottom of this README.

 Requirements
 ----------------
 - Python==3.8.5
 - Django==3.0.6
 - django-widget-tweaks==1.4.8
 - asgiref==3.2.10
 - pytz==2020.1
 - sqlparse==0.3.1

 How to Get Started
 ----------------
 1) Once Python is installed, install virtualenv: `$ pip install virtualenv`
 2) Create a virtual environment with this command: 
 `$ virtualenv --python C:\Users\{user_name}\AppData\Local\Programs\Python\Python38\python.exe env` or `$ virtualenv --python /usr/bin/python3.8 env`
 Your path to the python.exe may look different.
 3) Navigate inside the folder where you created the virtual environment. Run the following command: `$ .\env\Scripts\activate` or `$ source env/bin/activate`
 4) Run the following command: `$ pip install -r requirements.txt`
 5) Navigate to the *grewtix* dir and enter the following commands: 
 - `$ python manage.py makemigrations tickets`
 - `$ python manage.py migrate`
 6) Create a user so you can access the admin page: `$ python manage.py createsuperuser`
 7) Start the server: `$ python manage.py runserver`
 9) In your browser navigate to localhost:8000/admin. Create some tickets.
 10) Once you create test data, feel free to navigate through the application.

Features to add
---------------
 * UI design overhaul: give design to login, logout, and other random pages. Redesign ticket form and index, make it user friendly
 * create a dockerfile to run this application
 * setup the ticket claim button through ajax, make the call asynchronously 
 * limit viewability if not logged in
 * setup unit tests
 * add comment functionality
 * add attachment functionality
 * view all tickets by project (make it the homepage dashboard)
 * Create a simple reports page (total finished tickets, tickets finished by user)
 * Create a profile page
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

Reason for development
----------------------
This project started as a way to learn Python, but has turned into an ongoing project with the hopes of being a useful ticketing system. When I began this project, I had only worked with Youtrack, JetBrains ticketing system. You may be able to notice some similarities. 