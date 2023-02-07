import os
from numpy.typing import ArrayLike

from reipresoplot import plot_bar_graph


result_dir = "examples/using_graph_functions/result/"
os.makedirs(result_dir, exist_ok=True)

y_data: ArrayLike = [80, 70, 60, 90, 70]
x_data: list[str] = ["April", "May", "June", "July", "August"]
title: str = "Test Scores"
x_label: str = "Month held"
y_label: str = "Score [points]"

focus_indexes: list[int] = [1]
focus_color: str = "#00796B"

plot_bar_graph(
    y_data,
    x=x_data,
    title=title,
    x_label=x_label,
    y_label=y_label,
    focus_indexes=focus_indexes,
    color=focus_color,
    savefig_filepath=os.path.join(result_dir, "plot_bar_graph.png"),
)
