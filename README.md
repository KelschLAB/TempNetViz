# TempNetViz

**TempNetViz** is an interactive GUI designed for exploring, analyzing, and visualizing **temporal graphs** — graphs that evolve over time. This readme provides the essential information for the usage of TempNetViz, for more details see the [documentation](https://cnelias.github.io/TempNetVizDocs.github.io/).

## Installation & usage

You can install TempNetViz with pip using:

pip install tempnetviz

To start the GUI:

python -m tempnetviz.main_gui

## Quickstart

Your data should be stored in a single folder as **.csv files**, where each file represents the graph at a specific time point.

Steps to get started:

1. Click **Open** in the GUI to select the folder containing your `.csv` files.
2. Use the **Sub-graph selector** to choose one or multiple layers to visualize or analyze.
3. Adjust the **metrics** to explore structural properties of your data.
   You can apply a **graph cut** (edge pruning) for better readability on large graphs.
4. Switch between **Graph**, **Histogram**, and **Animation** views to gain different insights.

You can apply aesthetic changes (e.g. edge/nodes widths, colors...) to the results via the **settings** button.

![Quickstart](https://github.com/KelschLAB/TemporalGraphViz/raw/main/quickstart_numbered.png)

## Main Functionalities
Here we provide a short description of the main functionnalities of the GUI. For more information, see the [documentation](https://cnelias.github.io/TempNetVizDocs.github.io/)
### Structure Visualization

Visualize temporal graphs as a 3D stack to see how connections evolve over time. You can compute various metrics to quantify node importance — important nodes will appear larger.

![Graph Structure](https://github.com/KelschLAB/TemporalGraphViz/raw/main/3D_view.png)

### Metrics Distribution

Visualize how metrics evolve over time using histograms.

![Metrics Distribution](https://github.com/KelschLAB/TemporalGraphViz/raw/main/histo_view.png)

### Temporal Layout

You can also display the results as a temporal layout.

![Temporal Layout](https://github.com/KelschLAB/TemporalGraphViz/raw/main/temporal_layout.png)


### Graph Animation

Animate the temporal evolution of your graph to better understand dynamics.

![Graph Animation](https://github.com/KelschLAB/TemporalGraphViz/raw/main/graph_animation.gif)

## License

This project is licensed under the MIT License.
