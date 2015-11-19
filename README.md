# topside-control
Python scripts for joystick control (etc)

## Setting up Python on Windows

1. Download and run Python setup: https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi
2. Downlaod and run PyGame setup: http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi
3. Configure the python environment variables `PATH` and `PYTHONPATH`: http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7/4855685#4855685
4. Reboot your computer.  Not sure why it matters, but it matters.


## joystick-tester.py - For testing any joystick in particular

Running `python joystick-tester.py` will print out a list of joysticks were found, and their number (starting from 0).  Let's say it found (against all probability) joystick #37.

Running `python joystick-tester.py 37 1>output.log` will show a constantly-updating representation of the value of each joystick axis and the state of each button. The `1>output.log` is a hack -- normally a lot of debug messages get printed to the screen, and this redirects them to a file (which can be deleted) called `ouptut.log`.


## saitek_cyborg_evo_controller.py - for controlling Ian's $1 joystick

Assume joystick #37.

Running `python saitek_cyborg_evo_controller.py 37 1>output.log` runs the topside controller that interprets the donated joystick.