Overarching goal
================
The goal is to work together on projects down the road. This will hopefully be a small step towards that, starting with the design of this project through htm l and css.The focus will remain on html and css as not to bog down the collaboration efforts with the learning of Django.

Location of files
================
 * All the main html files will be found in this folder -- index, create, edit pages, as well as the footer/header: grewtix/tickets/templates/tickets
    * these files will need redesigned, css added, etc
 * All the files without any current design -- login, logout, delete_confirm, password_reset, etc -- are found here: grewtix/templates/registration
 * The ticket_confirm_delete.html is found here: grewtix/tickets/templates/tickets/ticket_confirm_delete.html
The css file that will be used is found at this location: grewtix/tickets/static/tickets/css/main.css
 * Feel free to make more css files if needed.

Other things to note
================
 * All functionality should already be included in the html pages. To move certain pieces that interact with the backend
  will require moving the parts between the brackets.
 * The majority of the html is currently using bootstrap. I have cdn referenced in the top of the header.html file.
 * I am I also using font awesome for all the fonts; the cdn is in the header.html file.
