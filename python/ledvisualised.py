#https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html
import matplotlib.pyplot as plt
from ledcube import create_cube

plt.style.use('_mpl-gallery')


# Make data
n = 5
xs, ys, zs = create_cube(n)
print(f"{xs}\n{ys}\n{zs}")

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs,c = zs)


ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()