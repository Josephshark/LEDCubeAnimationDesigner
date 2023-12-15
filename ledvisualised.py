#https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Pick a n for an nxnxn cube
n = 3

#Populate an array
x = np.array([])
starting_index = 0
for index in range(n*n*n):
    # if the index has reached 
    if (index+1)%9 == 0:




# Make data
xs = np.array([0, 1, 2])
ys = np.array([0, 1, 2])
zs = np.array([0, 1, 2])

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()