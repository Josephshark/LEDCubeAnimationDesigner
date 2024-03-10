import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ledcube as lc

n = 5
cube = lc.LedCube(n)
cube1 = cube

cube.change_led([0,0,0], 5) # Replace this with your own data
cube2 = cube

# create a columns around the first led
for z in range(n):
    cube.change_led([1,1,z], 5)
    cube.change_led([0,1,z], 5)
    cube.change_led([1,0,z], 5)

cube3 = cube

cubes = [cube1, cube2]

# Function to initialize the plot
def init():
    scatter = ax.scatter(cube1.x, cube1.y, cube1.z, c = cube1.brightness)
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
scatter = ax.scatter(cube1.x, cube1.y, cube1.z, c = cube1.brightness)

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Create the animation
animation = FuncAnimation(fig, update, frames=range(2), init_func=init, blit=False, interval=1000)

# Show the animation
plt.show()