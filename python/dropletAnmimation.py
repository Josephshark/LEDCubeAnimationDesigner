"""
Copyright <2024> <Joseph Bagheri>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ledcube as lc

# Set the nxnxn number for example for a 5x5x5 enter a 5
n = 5

# Empty cube
cube0 = lc.LedCube(n)

# Create a cube for each frame and define witch led to turn on
cube1 = lc.LedCube(n)
# Change the brightness of an led using the change led function:
    # change_led([x, y, z], brightness_value_of_the_chosen_LED)
cube1.change_led([2,2,4], 5) # Replace this with your own data
for i in range(n):
    for j in range(n):
        cube1.change_led([i,j,0], 5)

cube2 = lc.LedCube(n)
cube2.change_led([2,2,3], 5)
for i in range(n):
    for j in range(n):
        cube2.change_led([i,j,0], 5)

cube3 = lc.LedCube(n)
cube3.change_led([2,2,2], 5)
for i in range(n):
    for j in range(n):
        cube3.change_led([i,j,0], 5)

cube4 = lc.LedCube(n)
cube4.change_led([2,2,1], 5)
for i in range(n):
    for j in range(n):
        cube4.change_led([i,j,0], 5)

cube5 = lc.LedCube(n)
for i in range(1,4):
    for j in range(1,4):
        cube5.change_led([i,j,0], 5)
cube5.change_led([2,2,0], 0)

cube6 = lc.LedCube(n)
for i in range(n):
    cube6.change_led([i,0,0], 5)
    cube6.change_led([i,4,0], 5)
    cube6.change_led([0,i,0], 5)
    cube6.change_led([4,i,0], 5)
for i in range(1,4):
    for j in range(1,4):
        cube6.change_led([i,j,0], 0)
cube6.change_led([2,2,0], 5)

cube7 = lc.LedCube(n)
cube7.change_led([2,2,1], 5)
for i in range(n):
    for j in range(n):
        cube7.change_led([i,j,0], 5)
cube7.change_led([2,2,0], 0)

cube8 = lc.LedCube(n)
for i in range(n):
    for j in range(n):
        cube8.change_led([i,j,0], 5)

# The places where the cube frames are stored
cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8]

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