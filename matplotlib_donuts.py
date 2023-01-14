'''
In this program, the numpy library is used to create arrays of data for the x and y coordinates of the donut.
The matplotlib.pyplot library is used to create the figure and axes, and to plot the data.
The FuncAnimation class is used to create an animation of the donut rotating.

In simple terms, the program creates a circular shape using mathematical equations, then creates a function to update the shape's position
and rotates the shape using animation function.

The mathematical part is using Trigonometry functions (sine and cosine) to calculate the x and y coordinates of the points on the
circumference of the circle.
x = r * np.cos(theta) and y = r * np.sin(theta) this calculates the x and y coordinates for a circle of radius 'r' and parameterized by
theta (angle in radians).
The rotation of the donut is done by updating the theta value with a small angle increment in every iteration, thus creating
an animation of rotation.
line.set_data(r * np.cos(theta + num), r * np.sin(theta + num)) Here 'num' is the angle increment which is varied in every
iteration to give the rotation effect.
'''

import numpy as np
import matplotlib.pyplot as plt

# Create a figure and axes
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the data for the donut
r = 0.5
theta = np.linspace(0, 2 * np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the data as a line
line, = ax.plot(x, y)

# Define a function to update the plot
def update(num):
    line.set_data(r * np.cos(theta + num), r * np.sin(theta + num))
    return line,

# Use animation to repeatedly call the update function
from matplotlib.animation import FuncAnimation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), blit=True)

# Show the plot
plt.show()
