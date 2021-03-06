import numpy as np
from matplotlib import pyplot as plt, ticker as plticker
from pathlib import Path

# Create the two "linestring" paths as 2 vectors of (x,y) coordinates

v1 = np.array([(2, 5), (3, 5), (5, 3), (6, 3), (6, 2), (7, 1), (9, 3),])

v2 = np.array(
    [
        (9, 0),
        (5, 0),
        (6, 1),
        (5, 2),
        (4, 3),
        (3, 4),
        (2, 3),
        (1, 4),
        (0, 3),
    ]
)

v1_x, v1_y = v1[:, 0], v1[:, 1]
v2_x, v2_y = v2[:, 0], v2[:, 1]

v1_midpoints = (v1[:-1] + v1[1:]) / 2
v2_midpoints = (v2[:-1] + v2[1:]) / 2

v1_mid_dirs = v1[1:] - v1[:-1]
v2_mid_dirs = v2[1:] - v2[:-1]

v1_mid_x, v1_mid_y = v1_midpoints[:, 0], v1_midpoints[:, 1]
v2_mid_x, v2_mid_y = v2_midpoints[:, 0], v2_midpoints[:, 1]

v1_mid_dirs_x, v1_mid_dirs_y = v1_mid_dirs[:, 0], v1_mid_dirs[:, 1]
v2_mid_dirs_x, v2_mid_dirs_y = v2_mid_dirs[:, 0], v2_mid_dirs[:, 1]


def draw_plot():
    plt.figure(figsize=(15, 15))
    #plt.title("Two paths that approach nearby in opposite directions")
    ax = plt.axes()
    ax.set_aspect(1)
    for axis, label in zip([ax.xaxis, ax.yaxis], ["x", "y"]):
        loc = plticker.MultipleLocator(base=1)
        axis.set_major_locator(loc)
        axis.set_label_text(label, fontsize=20, rotation=0)
    plt.plot(v1_x, v1_y)
    plt.plot(v2_x, v2_y)
    plt.quiver(v1_mid_x, v1_mid_y, v1_mid_dirs_x, v1_mid_dirs_y, units="xy", scale=2.0)
    plt.quiver(v2_mid_x, v2_mid_y, v2_mid_dirs_x, v2_mid_dirs_y, units="xy", scale=2.0)
    plt.grid(which="both", linestyle="--")
    return

def show_plot():
    draw_plot()
    plt.show()
    return


def save_plot():
    file = Path(__file__).parent / "img" / "quiver_plot.png"
    draw_plot()
    plt.savefig(file, bbox_inches="tight")
    return

if __name__ == "__main__":
    show_plot()
