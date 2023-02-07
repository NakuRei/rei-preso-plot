from matplotlib import pyplot as plt
import os
from numpy.typing import ArrayLike

from reipresoplot import get_bar_graph_mpl_style_path


def test_plot(title: str, savefig_filepath: str):
    y_data: ArrayLike = [80, 70, 60, 90, 70]
    x_data: list[str] = ["April", "May", "June", "July", "August"]
    legends: list[str] = ["A", "B", "C"]
    x_label: str = "Month held"
    y_label: str = "Score [points]"

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.bar(x_data, y_data, width=0.7)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend(legends)

    fig.show()
    fig.savefig(savefig_filepath)


result_dir = "examples/using_matplotlibrc_files/result/"
os.makedirs(result_dir, exist_ok=True)

test_plot(
    title="Before",
    savefig_filepath=os.path.join(result_dir, "bar_graph_before.png"),
)

mpl_style_path: str = get_bar_graph_mpl_style_path()
with plt.style.context(mpl_style_path):
    test_plot(
        title="After",
        savefig_filepath=os.path.join(result_dir, "bar_graph_after.png"),
    )
