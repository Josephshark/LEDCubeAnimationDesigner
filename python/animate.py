import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ledcube as lc

# Set the nxnxn number for example for a 5x5x5 enter a 5
n = 5

# Create a cube for each frame and define witch led to turn on
cube1 = lc.LedCube(n)
# Change the brightness of an led using the change led function:
    # change_led([x, y, z], brightness_value_of_the_chosen_LED)
cube1.change_led([0,0,0], 5) # Replace this with your own data

cube2 = lc.LedCube(n)

# Repeat the same thing as cube one
cube2.change_led([0,0,0], 5)

# create a columns around the first led
for k in range(n):
    # Make a column at the x = 1, y = 1, position.
    cube2.change_led([1,1,k], 5)
    cube2.change_led([0,1,k], 5)
    cube2.change_led([1,0,k], 5)

# Makes an empty cube
cube3 = lc.LedCube(n)

# Start a wave
cube4 = lc.LedCube(n)

for i in range(n):
    cube4.change_led([i,0,0], 5)
    cube4.change_led([i,n-1,0], 5)

cube5 = lc.LedCube(n)
for i in range(n):
    # Left wave
    cube5.change_led([i,0,0], 5)
    cube5.change_led([i,0,1], 5)
    cube5.change_led([i,1,0], 5)

    # Right Wave 
    cube5.change_led([i,n-1,0], 5)
    cube5.change_led([i,n-1,1], 5)
    cube5.change_led([i,n-2,0], 5)

cube6 = lc.LedCube(n)
for i in range(n):
    # Left wave
    cube6.change_led([i,0,0], 5)
    cube6.change_led([i,1,0], 5)
    cube6.change_led([i,1,1], 5)
    cube6.change_led([i,2,0], 5)

    # Right Wave 
    cube6.change_led([i,n-2,0], 5)
    cube6.change_led([i,n-2,1], 5)
    cube6.change_led([i,n-3,0], 5)
    cube6.change_led([i,n-1,0], 5)

cube7 = lc.LedCube(n)
for i in range(n):
    # One Wave
    cube7.change_led([i,1,0], 5)
    cube7.change_led([i,2,0], 5)
    cube7.change_led([i,2,1], 5)
    cube7.change_led([i,2,2], 5)
    cube7.change_led([i,2,3], 5)
    cube7.change_led([i,n-2,0], 5)

cube8 = lc.LedCube(n)
for i in range(n):
    # Left wave
    cube8.change_led([i,0,0], 5)
    cube8.change_led([i,1,0], 5)
    cube8.change_led([i,1,1], 5)
    cube8.change_led([i,2,0], 5)

    # Right Wave 
    cube8.change_led([i,n-2,0], 5)
    cube8.change_led([i,n-2,1], 5)
    cube8.change_led([i,n-3,0], 5)
    cube8.change_led([i,n-1,0], 5)

cube9 = lc.LedCube(n)
for i in range(n):
    # Left wave
    cube9.change_led([i,0,0], 5)
    cube9.change_led([i,0,1], 5)
    cube9.change_led([i,1,0], 5)

    # Right Wave 
    cube9.change_led([i,n-1,0], 5)
    cube9.change_led([i,n-1,1], 5)
    cube9.change_led([i,n-2,0], 5)

# The places where the cube frames are stored
cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9]

# Function to initialize the plot
def init():
    cube0 = lc.LedCube(n)
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
scatter = ax.scatter(cube1.x, cube1.y, cube1.z, c = cube1.brightness)

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Create the animation
animation = FuncAnimation(fig, update, frames=range(len(cubes)), init_func=init, blit=False, interval=1000)

# Show the animation
plt.show()