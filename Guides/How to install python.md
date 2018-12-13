How to Install Python: 

https://www.python.org/downloads/
Download latest python version (3.7+) and install.it
It will have
PIP: command line uitility that can be used to install other python packages that help you in coding etc
Tkinter / IDLE: Tkinter is the GUI development package. IDLE is for coding interface. (App to write python code in)
Python test suit
Py Launcher (PEP) : Utility that is used by windows to decide how to execute a file with .py extension. (It's the exe that executes .py file?)

After you install python, open command prompt and run command ‘python’. If it runs successfully then it will open the python prompt

If you get an error like python is not recognized, then you need to edit your windows PATH environment variable to put path of your python.exe. Google this stuff if you don't know what environment variables are. If system environment variable is not accessible then you can a new define or use existing User environment variable for this. Just remember to close and start your command prompt again after you modify the path variable.
http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7


Pip Upgrade:
It's a package management system
PIP is already installed with python 3+, just upgrade using below.
 python -m pip install -U pip

You may also need to add path to the PIP script folder to your PATH environment variable.


Selenium webdriver
If you have pip on your system, you can simply install or upgrade the Python bindings:
pip install -U selenium

Editor/IDE
Next we need an IDE or editor. For now i am going with Atom.

Go to https://atom.io/ download and install atom text editor

Go through https://flight-manual.atom.io/ when you are bored.


For packages that help with python, follow this (It has screenshots for mac version so file menu is somewhat different for windows version) 
https://hackernoon.com/setting-up-a-python-development-environment-in-atom-466d7f48e297

To install themes:
Open Atom> File > Settings > Install > Themes tab > 

Packages that should be installed
Hydrogen
	
Hydrogen-launcher
pip install jupyter
	pip install ipython	
Autocomplete-python
Linter-flake8 
(For this to work properly you also need to install python package for this on command prompt by using pip install flake8)
Minimap (Not required right now)
Python-autopep8
	(pip install autopep8)
Script

Disadvantages of Atom that I noticed:
There is no progress bar when installing a theme/package
There is no support for command line input out of the box. Trying hydrogen package for that.
Hydrogen works, but it took a lot of time to Setup. Also i don't know exact steps that i took to finally make it work (reinstalling hydrogen) So not sure if i can help with that to anyone else.
