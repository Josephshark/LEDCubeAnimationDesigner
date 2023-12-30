from blitmanager import BlitManager
import matplotlib.pyplot as plt
import numpy as np

# make a new figure
fig, ax = plt.subplots()

# add a line
x = np.linspace(0, 2 * np.pi, 100)
(ln,) = ax.plot(x, np.sin(x), animated=True)

# add a frame number
fr_number = ax.annotate(
    "0",
    (0, 1),
    xycoords="axes fraction",
    xytext=(10, -10),
    textcoords="offset points",
    ha="left",
    va="top",
    animated=True,
)
bm = BlitManager(fig.canvas, [ln, fr_number])
# make sure our window is on the screen and drawn
plt.show(block=False)
plt.pause(.1)

for j in range(1000):
    # update the artists
    ln.set_ydata(np.sin(x + (j / 1000) * np.pi))
    fr_number.set_text(f"frame: {j}")
    # tell the blitting manager to do its thing
    bm.update()