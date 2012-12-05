Google Status Changer v1.0
==========================

This is a simple application to change your gmail/gtalk status periodically with a set of statuses. 
This comes in handy when its annoying to manually change your status time to time.

- An executable for linux is available here: http://dl.dropbox.com/u/30013949/gstatus-ch
- Download the executable and run the command "chmod +x gstatus-ch" to give executable permissions. 
- run "./gstatus-ch" in your terminal to launch it. Enjoy!
- An executable for windows is available here: http://dl.dropbox.com/u/30013949/gStatusChanger.exe


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

+ #1 radio buttons for 'default' and 'dnd' status (green and red)
+ #2 restrict interval box with numbers
+ #3 menubar
+ Future release :
	- #4 features to set status by time of day. (must have)
	- #5 full length email-id support (must have)
	- #6 better authentication ways (better to have)
+ #6 help
+ #7 disclaimer
+ #8 remove wordwrapping and introduce HBar for status box
+ #9 Improve UI


Changelog
=========

version 1.0 (Initial Relase)
+ Basic UI
+ Supports multiple statuses
