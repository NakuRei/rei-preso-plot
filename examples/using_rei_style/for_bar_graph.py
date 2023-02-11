from matplotlib import pyplot as plt
import os
from numpy.typing import ArrayLike

from reipresoplot import use_bar_graph_style_as_global_settings

use_bar_graph_style_as_global_settings()

y_data: ArrayLike = [80, 70, 60, 90, 70]
x_data: list[str] = ["April", "May", "June", "July", "August"]
legends: list[str] = ["A", "B", "C"]
x_label: str = "Month held"
y_label: str = "Score [points]"
title: str = "Title"

result_dir = "examples/using_rei_style/result/"
os.makedirs(result_dir, exist_ok=True)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(x_data, y_data, width=0.7)

ax.set_title(title)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.legend(legends)

fig.show()
fig.savefig(os.path.join(result_dir, "for_bar_graph.png"))
