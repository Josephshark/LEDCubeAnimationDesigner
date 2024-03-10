# Sample data
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import ledcube as lc

n = 5
cube = lc.LedCube(n)
cube.change_led([0,0,0], 5)

data1 = cube.brightness
#print(data1)

# create a columns around the first led
for z in range(n):
    cube.change_led([1,1,z], 5)
    cube.change_led([0,1,z], 5)
    cube.change_led([1,0,z], 5)

data2 = cube.brightness
print(data2)

data = np.random.rand(3, 10)  # Replace this with your own data
#print(data)