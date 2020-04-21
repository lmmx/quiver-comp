import numpy as np
from matplotlib import pyplot as plt, ticker as plticker
from pathlib import Path
from interpolate_coords import adjacent_pairs, interpolate_1d, interpolate_2d, interpolate_y_vals
from doubleback_quiver import v1, v2

v1_i = interpolate_2d(v1)
v2_i = interpolate_2d(v2)

v1_i_x, v1_i_y = v1_i[:,0], v1_i[:,1]
v2_i_x, v2_i_y = v2_i[:,0], v2_i[:,1]

def draw_plot(prune_quiver_rate=4):
    # Create quiver x, y, u, and v then prune
    q1x, q1y = v1_i_x[:-1], v1_i_y[:-1]
    q1u, q1v = v1_i_x[1:] - v1_i_x[:-1], v1_i_y[1:] - v1_i_y[:-1]
    q2x, q2y = v2_i_x[:-1], v2_i_y[:-1]
    q2u, q2v = v2_i_x[1:] - v2_i_x[:-1], v2_i_y[1:] - v2_i_y[:-1]
    q1x, q1y, q1u, q1v = [q[::prune_quiver_rate] for q in [q1x, q1y, q1u, q1v]]
    q2x, q2y, q2u, q2v = [q[::prune_quiver_rate] for q in [q2x, q2y, q2u, q2v]]

    plt.figure(figsize=(15, 15))
    # plt.title("Two paths that approach nearby in opposite directions")
    ax = plt.axes()
    ax.set_aspect(1)
    c1, c2 = "green", "purple"
    for axis, label in zip([ax.xaxis, ax.yaxis], ["x", "y"]):
        loc = plticker.MultipleLocator(base=1.0)
        axis.set_major_locator(loc)
        axis.set_label_text(label, fontsize=20, rotation=0)
    plt.plot(v1_i_x, v1_i_y, linestyle="--", color=c1)
    plt.quiver(q1x, q1y, q1u, q1v, scale_units='xy', angles='xy', scale=1.5, color=c1)
    plt.plot(v2_i_x, v2_i_y, linestyle="--", color=c2)
    plt.quiver(v2_i_x[:-1], v2_i_y[:-1], v2_i_x[1:]-v2_i_x[:-1], v2_i_y[1:]-v2_i_y[:-1],
               scale_units='xy', angles='xy', scale=1.5, color=c2)
    #plt.grid(which="both", linestyle="--")
    return


def show_plot():
    draw_plot()
    plt.show()
    return


if __name__ == "__main__":
    show_plot()
