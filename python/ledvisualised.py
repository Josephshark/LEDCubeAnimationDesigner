#https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html
import ledcube as lc
import matplotlib.animation as animation

n = 5
cube = lc.LedCube(n)
cube.change_led([0,0,0], 5)

# create a columns around the first led
for z in range(n):
    cube.change_led([1,1,z], 5)
    cube.change_led([0,1,z], 5)
    cube.change_led([1,0,z], 5)

cube.show()