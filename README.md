# Indee
functional test for user signup Indee

# Installation and setup

# Install python 3.6.1 : 
https://www.python.org/downloads/windows/
•	Click Download Python latest.
•	Click run
•	Click continue a few times. Agree to the terms and install. 
To verify Python Version type “python --version” on terminal.

# Install pip and virtualenv
	sudo apt-get install python-pip
	sudo pip install virtualenv

# Create a dir in which to install your virtualenv environment, and install and activate a new env
	mkdir mytests && cd $_
	virtualenv env
	source env/bin/activate

# install Django:
On the terminal type “sudo pip install django”.

# install selenium:
      On the terminal type “sudo pip install selenium” on path -> C:\Python36-32\Scripts
# Download and install chrome and Firefox driver:
Chrome - > https://sites.google.com/a/chromium.org/chromedriver/downloads

Firefox ->    https://github.com/mozilla/geckodriver/releases
Download this file and place this file in C:\Python36-32

# Set Environment Variable:
	Open control Panel -> System & Security -> System ->Advanced System
	Environment Variable button
	Select Path and click edit 
	Add C:\Python36-32 or whatever your python directory is.


