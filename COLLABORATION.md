Overarching goal
================
The goal is to work together on projects down the road. This will hopefully be a small step towards that, starting with the design of this project through html and css.The focus will remain on html and css as not to bog down the collaboration efforts with the learning of Django.

Development process
================
The development process will start with the repo being cloned. Please create a new branch that you will work under (ex. AveryS, TomC). Once you are finished with your designs, create a pull request to merge to the <em>develop-redesign</em> branch.

Location of files
================
 * All the main html files (index, create, edit pages, as well as the footer/header) will be found in this folder: grewtix/tickets/templates/tickets
    * these files will need redesigned, css added, etc
 * All the files without any current design (login, logout, delete_confirm, password_reset, etc) are found here: grewtix/templates/registration
 * The ticket_confirm_delete.html is found here: grewtix/tickets/templates/tickets/ticket_confirm_delete.html
 * The css file that will be used is found at this location: grewtix/tickets/static/tickets/css/main.css
 * Feel free to make more css files if needed.

Other things to note
================
 * All functionality should already be included in the html pages. To move certain pieces that interact with the backend
  will require moving the parts between the brackets.
      * <em>Ex. {% for ticket in ticket_list %}</em>
 * The majority of the html is currently using bootstrap. The cdn is referenced in the top of the header.html file.
 * I am I also using font awesome for all the fonts; the cdn is in the header.html file.
 * I have also created different queues (personal queue for the user logged in, queues of all unassigned tickets, and a queue for all tickets created by user)
   * In Django you can reference these files in any html file with
      * href="{% url 'tickets:my_queue' %}
      * href="{% url 'tickets:unassigned_queue' %}
      * href="{% url 'tickets:created_by_user_queue' %}


Design
================
 * You have total freedom on how you would like to design this.
 * When planning this, I was trying to mimic youtrack, so there are some similiraties.
   * Mimicking the design of youtrack may be a good starting point for designing this project. I don't have a preference either way, but this may help get the ball rolling.

Here's a pic of the home page queue on youtrack:

![Youtrack Queue](https://www.jetbrains.com/youtrack/img/screenshots/70/Issue_list@2x.png)

I created my own design mock-up that I think would work best. You can view the mock-up (here)[https://www.figma.com/file/HC2X9khLUbBmUl4FErxAeN/Grewtix?node-id=0%3A1]

 * I have still have plenty of features missing. For example, if trying to design a search bar, feel free to design the search bar. That feature will be added later, but the html can be added now. 
 * While designing, if you come up with other features that should be added: new icons, buttons, etc, please add them to your branch's collobaration.md below.
 
Features to add
================
List any feature you would like to see added here.
- add a "coming soon" page
