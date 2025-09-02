# Settings Overview  

The **Settings Window** lets you customize how graphs are displayed and explored in TempGraphViz.  
It is organized into **four tabs**:  

- [General](#general-settings)  
- [Graph Plot](#graph-plot-settings)  
- [Histogram](#histogram-settings)  
- [Animation](#animation-settings)  

---

## General Settings  

These options control the overall appearance and interpretation of your graph:  

- **Remove index row in input** – Ignore the first row/column of the input file. This is useful if your data contains labels or indices for the nodes. 
They can be displayed using ```show node labels```(see below) but should not be included in the analysis.
- **Show node labels** – Display labels for nodes. This will only work if your data has an indexing row/column. Otherwise, node numbers will be displayed.  
- **Edge type** – Choose whether your data represents **affinity** (similarity) or **distance** (dissimilarity). This determines the way the metrics are computed.  
- **Community detection algorithm** – Select with which algorithm groups of nodes are identified and clustered (`louvain`, `walktrap`, `infomap`, `modularity`).  
- **Remove feedback loops in plots** – Hide self-connections (nodes linked to themselves).  
- **Scale edge width** – Make edge thickness proportional to edge weight.  
- **Edge thickness** – Manually set the thickness of all edges.  
- **Node thickness** – Manually set the thickness of all nodes.  
- **Colormap for node metrics** – Pick a color scheme for node-related values (`Greys`, `Reds`, `Greens`, `Blues`, `cool`, `coolwarm`, `viridis`, `none`).  
- **Colormap for edge values** – Pick a color scheme for edge-related values (`Greys`, `Reds`, `Greens`, `Blues`, `cool`, `coolwarm`, `viridis`).  

---

## Graph Plot Settings  

These options affect how the graph itself is displayed:  

- **Multilayer display** – Choose between a **3D multilayer view** (layers superposed in a stack, making structure more explicit) or an **average projection** (all layers combined).  
- **Show planes** – Toggle background planes in 3D plots.  
- **Draw edges between layers** – Show or hide visual guidelines between nodes across different layers.  

---

## Histogram Settings  

These options control how distributions of values are displayed:  

- **Histogram type** – Choose between **side-by-side** histograms or **stacked** histograms.  
- **Show legend** – Toggle the legend on or off.  

---

## Animation Settings  

These options configure animations of temporal graphs:  

- **Time between frames (ms)** – Set how fast the animation runs by choosing the delay between frames (in milliseconds).  

---

## Notes  

- **Changes are applied immediately** when you toggle a setting or enter a value.  
- For numeric settings (e.g., edge thickness, node thickness, animation speed), press **Enter** after typing to apply the change.  
- Some settings depend on others (e.g., node labels require an index row).  

---
