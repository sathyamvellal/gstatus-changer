Google Status Changer v1.0
==========================

This is a simple application to change your gmail/gtalk status periodically with a set of statuses. 
This comes in handy when its annoying to manually change your status time to time.

- An executable for linux is available here: http://dl.dropbox.com/u/30013949/gstatus-ch
- Download the executable and run the command "chmod +x gstatus-ch" to give executable permissions. 
- run "./gstatus-ch" in your terminal to launch it. Enjoy!



Dependencies
============

+ Requires xmpp extensions for python. (pyxmpp or xmpppy)
+ Requires PyQt4
+ Requires pyuic4 to convert .ui to .py


Instructions
============

- To run : python2 main.py
- Enter the username and password. Enter only the username, not the email.
	Eg: username@gmail.com => Enter 'username' only
- Enter the interval in seconds
- Enter the statuses you want to set in the text box. Each status must be in a new line
- Click on start to begin the round-robin changing of your statuses!
- Click on stop to end.


TODO
====

+ radio buttons for 'default' and 'dnd' status (green and red)
+ restrict interval box with numbers
+ menubar
+ Future release - features to set status by time of day. (requested)
+ help
+ disclaimer
+ remove wordwrapping and introduce HBar for status box
+ Improve UI


Changelog
=========

version 1.0 (Initial Relase)
+ Basic UI
+ Supports multiple statuses
