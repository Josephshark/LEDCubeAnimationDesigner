import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ledcube as lc

# Set the nxnxn number for example for a 5x5x5 enter a 5
n = 5
cubes = []
cube0 = lc.LedCube(n)
numframes = 20
for f in range(numframes):
    icube = lc.LedCube(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if random.random() > 0.5:
                    icube.change_led([i,j,k],5*random.random())
    cubes.append(icube)

# Function to initialize the plot
def init():
    scatter = ax.scatter(cube0.x, cube0.y, cube0.z, c = cube0.brightness)
    return (ax,)

# Function to update the plot at each frame
def update(frame):
    # Update the data for each frame (replace this with your own data update logic)
    # update the index
    
    # Clear the previous scatter plot
    ax.cla()
    
    # Plot the updated data
    ax.scatter(cubes[frame].x, cubes[frame].y, cubes[frame].z, c = cubes[frame].brightness)
    
    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    return (ax,)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the initial data
scatter = ax.scatter(cube0.x, cube0.y, cube0.z, c = cube0.brightness)

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Create the animation
animation = FuncAnimation(fig, update, frames=range(len(cubes)), init_func=init, blit=False, interval=100)

# Show the animation
plt.show()