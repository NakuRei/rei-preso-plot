import os
from numpy.typing import ArrayLike

from reipresoplot import plot_line_graph


result_dir = "examples/using_graph_functions/result/"
os.makedirs(result_dir, exist_ok=True)


y_data: ArrayLike = [
    [80, 70, 60, 90, 70],
    [50, 60, 70, 80, 90],
    [90, 95, 90, 80, 100],
]
x_data: list[str] = ["April", "May", "June", "July", "August"]
legends: list[str] = ["A", "B", "C"]
title: str = "Test Scores"
x_label: str = "Month held"
y_label: str = "Score [points]"

focus_indexes: list[int] = [1]
focus_color: str = "#00796B"

plot_line_graph(
    y_data,
    x=x_data,
    legends=legends,
    title=title,
    x_label=x_label,
    y_label=y_label,
    focus_indexes=focus_indexes,
    focus_color=focus_color,
    savefig_filepath=os.path.join(result_dir, "plot_line_graph.png"),
)
