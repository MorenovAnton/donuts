import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Create the data for the donut
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
r = 0.5

# Parametric equation of a torus
x = (r + r * np.cos(v)) * np.cos(u)
#x = x.reshape(100,100)
y = (r + r * np.cos(v)) * np.sin(u)
#y = y.reshape(100,100)
z = r * np.sin(v)
#z = z.reshape(100,100)

# Plot the data as a surface
surf = ax.plot_surface(x, y, z)

# Define a function to update the plot
def update(num):
    ax.view_init(elev=10., azim=num)
    return surf,

# Use animation to repeatedly call the update function
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 360, 100), blit=True)

# Show the plot
plt.show()
