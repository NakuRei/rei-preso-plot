# rei-preso-plot

Python package for drawing graphs for presentation materials with `matplotlib`.

## Description

A package for creating graphs suitable for presentation materials with `matplotlib`.
The created graph can be directly placed on a presentation slide with a nice design.

## Requirement

- Python 3.11.1
- matplotlib 3.6.3

## Installation

```shell
pip install reipresoplot
```

## Usage

### Using graph functions

Graph functions.
Can emphasize parts by adding color or embedding legends in line graphs.
When passing `matplotlib.axes.Axes` to the argument ax, it returns the `matplotlib.axes.Axes`. Therefore, using the functions of `matplotlib`, you can specify the drawing range, etc., after these functions.

| 関数                           | 説明                        |
| :----------------------------- | :-------------------------- |
| `reipresoplot.plot_line_graph` | Line graph drawing function |
| `reipresoplot.plot_bar_graph`  | Bar graph drawing function  |

#### Plot line graph

Running [examples/using_graph_functions/for_line_graph.py](examples/using_graph_functions/for_line_graph.py) will produce the following graph.

![plot_line_graph](examples/using_graph_functions/result/plot_line_graph.png)

#### Plot bar graph

Running [examples/using_graph_functions/for_bar_graph.py](examples/using_graph_functions/for_bar_graph.py) will produce the following graph.

![plot_bar_graph](examples/using_graph_functions/result/plot_bar_graph.png)

### Using matplotlibrc files

By reading `matplotlibrc` files, you can customize the `matplotlib` style as a whole, i.e. without specifying it with `rcParams`, etc.
For details, see [Matplotlib documentation](https://matplotlib.org/stable/tutorials/introductory/customizing.html).

| 関数                                         | 説明                                                    |
| :------------------------------------------- | :------------------------------------------------------ |
| `reipresoplot.get_line_graph_mpl_style_path` | Get the path to the `matplotlibrc` file for line graphs |
| `reipresoplot.get_bar_graph_mpl_style_path`  | Get the path to the `matplotlibrc` file for bar graphs  |

If you want to apply the style globally to the entire graph plot, use `plt.style.use`.

```python
from matplotlib import pyplot as plt
from reipresoplot import get_line_graph_mpl_style_path

mpl_style_path: str = get_line_graph_mpl_style_path()
plt.style.use(mpl_style_path)

plt.plot(x, y)
plt.show()
```

If you want to use it temporarily, use a context manager.

```python
mpl_style_path: str = get_line_graph_mpl_style_path()
with plt.style.context(mpl_style_path):
    plt.plot(x, y)
    plt.show()
```

#### Line graph changes

Please refer to the code at [examples/using_matplotlibrc_files/for_line_graph.py](examples/using_matplotlibrc_files/for_line_graph.py) for line graph changes.

|                                  before                                   |                                  after                                  |
| :-----------------------------------------------------------------------: | :---------------------------------------------------------------------: |
| ![before](examples/using_matplotlibrc_files/result/line_graph_before.png) | ![after](examples/using_matplotlibrc_files/result/line_graph_after.png) |

#### Bar graph changes

Please refer to the code at [examples/using_matplotlibrc_files/for_bar_graph.py](examples/using_matplotlibrc_files/for_bar_graph.py) for bar graph changes.

|                                  before                                  |                                 after                                  |
| :----------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| ![before](examples/using_matplotlibrc_files/result/bar_graph_before.png) | ![after](examples/using_matplotlibrc_files/result/bar_graph_after.png) |

## Test

You can test graph drawing with Pytest.

```shell
pytest
```

## Author

[NakuRei](https://notes.nakurei.com/about/)

## License

© 2023 NakuRei

This software is released under the MIT License, see LICENSE.