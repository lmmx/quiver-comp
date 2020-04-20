import numpy as np
from matplotlib import pyplot as plt, ticker as plticker
from pathlib import Path

# Create the two "linestring" paths as 2 vectors of (x,y) coordinates

# Green, above
v1 = np.array(
    [
        (9.0, 4.5),
        (1.0, 3.0),
        (4.2, 3.0),
        (5.5, 2.5),
        (3.0, 0.8),
        (4.5, 0.8),
    ]
)

# Purple, below (doubling back)
v2 = np.array(
    [
        (8.0, 0.5),
        (2.0, 0.5),
        (4.7, 2.3),
        (4.1, 2.7),
        (3.7, 2.6),
        (4.1, 2.2),
        (0.0, 2.3),
        (0.8, 3.4),
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
    # plt.title("Two paths that approach nearby in opposite directions")
    ax = plt.axes()
    ax.set_aspect(1)
    for axis, label in zip([ax.xaxis, ax.yaxis], ["x", "y"]):
        loc = plticker.MultipleLocator(base=1.0)
        axis.set_major_locator(loc)
        axis.set_label_text(label, fontsize=20, rotation=0)
    plt.plot(v1_x, v1_y, linestyle="--", color="green")
    plt.plot(v2_x, v2_y, linestyle="--", color="purple")
    plt.quiver(v1_mid_x, v1_mid_y, v1_mid_dirs_x, v1_mid_dirs_y, units="xy", scale=2.0, color="green")
    plt.quiver(v2_mid_x, v2_mid_y, v2_mid_dirs_x, v2_mid_dirs_y, units="xy", scale=2.0, color="purple")
    #plt.grid(which="both", linestyle="--")
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
