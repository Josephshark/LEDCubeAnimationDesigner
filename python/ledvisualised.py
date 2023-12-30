#https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html

import ledcube as lc

n = 5
cube = lc.LedCube(n)
cube.change_led([0,0,0], 5)
cube.change_led([3,2,2], 5)
cube.show()
