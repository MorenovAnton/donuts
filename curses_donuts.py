'''
This program uses the curses library to create a terminal-based animation of a rotating donut. The math library is used to
perform calculations, and the time library is used to control the animation speed.

In this program, the curses.initscr() function is used to initialize the curses library and create a screen object that represents
the terminal window. curses.noecho() and curses.curs_set(0) are used to disable echoing of typed characters and to hide
the cursor respectively.

The program creates the data for the donut using the mathematical equations of rotation, it uses mathematical equations similar to
the previous example, but instead of plotting the points on the circumference of the circle, it uses the coordinates
to create a '*' on the terminal screen.
x = int(i * math.cos(theta) - j * math.sin(theta) + width / 2) and
y = int(i * math.sin(theta) + j * math.cos(theta) + height / 2)
this calculates the x and y coordinates for a circle of radius 'r' and parameterized by theta (angle in radians).

The while loop is used to update the theta value with a small angle increment in every iteration, thus creating an animation of rotation.
theta += 0.1 Here, we are incrementing the angle by 0.1 radians in every iteration which gives the rotation effect.

Finally, the screen.refresh() function is used to refresh the screen, and the time.sleep(0.05) function is used to pause the
program for a short time to create the animation effect.

Note: This program is meant to be run in the terminal and not in a Jupyter notebook.
This equation is using the mathematical concepts of Trigonometry, specifically the properties of rotation in 2-D plane.
'''

import curses
import math
import time

# Initialize curses and create a screen object
screen = curses.initscr()                        # initialize the curses library
# disable echoing of typed characters and to hide the cursor respectively
curses.noecho()
curses.curs_set(0)

# get the dimensions (height and width) of the terminal screen. The getmaxyx() method returns the number of rows and columns of
# the terminal window in the form of tuple (height, width)
height, width = screen.getmaxyx()

# In the line r = int(min(height, width) / 3), we are defining the radius of the donut. We are using min(height, width)
# because we want to make sure that the donut fits inside the terminal window, regardless of whether the window is taller or wider.
r = int(min(height, width) / 3)

# In the line theta = 0, we are initializing the angle theta to zero. theta is used as a parameter in the mathematical equations
# that calculate the x and y coordinates of the donut.
# The value of theta represents the angle in radians and is used to rotate the donut. Initially, we are setting it to zero, so the
# donut is drawn in its starting position (not rotated). In the while loop, theta is incremented by a small value in every iteration,
# which creates the rotation animation.
# theta += 0.1 here we are incrementing the angle by 0.1 radians in every iteration, thus creating the rotation animation.
# In simple terms, the variable theta is used to control the rotation of the donut, initially, it is set to zero and later on
# incremented by a small value in every iteration, which results in the animation of rotation of the donut.
theta = 0



while True:
    # Clear the screen
    screen.clear()

    # Draw the donut
    # are used to iterate through all the points on the circumference of the donut.
    # The value of i and j are used to calculate the x and y coordinates of each point on the circumference of the donut.
    for i in range(r):
        for j in range(r):
            # The i and j values are used as the coordinates of a point on the circumference of the donut in a reference system where
            # the center of the donut is the origin (0,0) and i is the distance of the point from the origin along the x-axis and j is the
            # distance of the point from the origin along the y-axis.
            # The math.cos(theta) and math.sin(theta) functions are used to calculate the cosine and sine of the angle theta respectively.
            # The x-coordinate of the point is obtained by rotating the point by an angle theta in the counter-clockwise direction. The rotation matrix for 2D rotation is:
            '''
            [cos(theta) -sin(theta)]
            [sin(theta)  cos(theta)]
            '''
            # The new x-coordinate is given by:
            # x = i*cos(theta) - j*sin(theta)
            # The width/2 term is added to center the donut on the screen, this is done by shifting the x-coordinate of the donut to the center of the screen by adding (width/2) to the x-coordinate.
            x = int(i * math.cos(theta) - j * math.sin(theta) + width / 2)
            y = int(i * math.sin(theta) + j * math.cos(theta) + height / 2)
            # is used to determine if a point on the circumference of the donut should be plotted or not.
            # The statement i*i + j*j > r*r*0.7 checks if the distance of a point from the center of the donut is greater
            # than 70% of the radius of the donut. The statement i*i + j*j < r*r checks if the distance of a point from the center of the
            # donut is less than the radius of the donut.
            # The i*i + j*j part of the statement calculates the distance of a point from the center of the donut. This is done by
            # taking the square of the x and y coordinates of the point and adding them. The distance formula is given by:
            # distance = sqrt(x^2 + y^2)
            # since we are just comparing the distance with the radius of the donut, we can avoid the square root operation and use x^2 + y^2 instead.
            if (i*i + j*j > r*r*0.7) and (i*i + j*j < r*r):
                # plots a '*' at the point (x,y) on the terminal screen.
                screen.addch(y, x, '*')

    # Update theta for rotation
    # theta += 0.1 Here, we are incrementing the angle by 0.1 radians in every iteration which gives the rotation effect.
    theta += 0.1

    # Refresh the screen
    # screen.refresh() function is used to refresh the screen, and the time.sleep(0.05) function is used to pause the
    screen.refresh()
    # Sleep for a short time to create animation
    time.sleep(0.05)

# Exit curses
curses.endwin()




