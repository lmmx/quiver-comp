from matplotlib import pyplot as plt
from pathlib import Path
from doubleback_quiver import draw_plot

def show_plot():
    draw_plot()
    plt.show()
    return


def save_plot():
    file = Path(__file__).parent / "img" / "doubleback_plot.png"
    draw_plot()
    plt.savefig(file, bbox_inches="tight")
    return

if __name__ == "__main__":
    save_plot()
