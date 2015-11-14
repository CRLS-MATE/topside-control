import os
import sys
import time
import select
import pygame

# this is the number of dots that will be used to display the output of an axis
dots = 8

# this is for pygame
screen = None

# write to stderr.  pygame clutters up stdout because of a bug
def wrerr(msg):
    sys.stderr.write(msg)

# print to stderr to avoid SDL messages
def prerr(msg):
    wrerr(msg + "\r\n")

# write out all the information we know about a joystick
def printJoystickInfo(index, js):
    prerr("\n")
    prerr("Joystick %d: %s" % (index, js.get_name()))
    prerr("\tAxes:\t%d" % js.get_numaxes())
    prerr("\tBalls:\t%d" % js.get_numballs())
    prerr("\tButtons:\t%d" % js.get_numbuttons())
    prerr("\tHats:\t%d" % js.get_numhats())


# read joystick info and print it out on the screen
def readJoystick(js):
    pygame.event.pump()

    # cycle through all joystick axes
    for i, axis in enumerate([js.get_axis(i) for i in range(js.get_numaxes())]):
        norm = (axis + 1.0) / 2.0 # normalize to the range 0-1

        # print the axis number
        wrerr(str(i) + ": ")
        # print an exclamation point if the value is above this dot, otherwise a period
        for d in range(dots):
            if d < norm * dots:
                wrerr("!")
            else:
                wrerr(".")

        wrerr("\t")

    # print a -- if the button is not pressed, print the button number if it is pressed
    for i, button in enumerate([js.get_button(i) for i in range(js.get_numbuttons())]):
        if button:
            wrerr(str(i))
        else:
            wrerr("-" * len(str(i)))

    prerr("")




# normal script entry
if __name__ == "__main__":

    # set up pygame, including a screen (even though we don't need it)
    global screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # print error message if no joysticks were connected
    if pygame.joystick.get_count() < 1:
        prerr("No joysticks were found :(")
        exit(1)

    # print info about each joystick that was found
    for i, js in enumerate([pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]):
        js.init()
        printJoystickInfo(i, js)
        prerr("")

    # print an error message if no joystick was specified
    if len(sys.argv) < 2:
        pygame.quit()
        prerr("Monitor a specific joystick with the command 'python %s <joystick number> 1>/dev/null'" % sys.argv[0])
        exit(1)

    # initialize the joystick that was specified on the command line
    js = pygame.joystick.Joystick(int(sys.argv[1]))
    if not js.get_init():
        js.init()

    # loop and read input
    while True:
        readJoystick(js)

        if "darwin" == sys.platform
            # wait for a keypress, and exit if we get one
            i, o, e = select.select( [sys.stdin], [], [], 0.01 )
            if i:
                pygame.quit()
                break
