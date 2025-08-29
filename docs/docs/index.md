# Multilayer Graph Analysis GUI

This software provides an interactive **graph analysis and visualization tool** with a graphical user interface (GUI).  
It is designed for exploring, analyzing, and visualizing multilayer graphs stored as CSV files.

---




## 🚀 Quickstart
1. Click **Open** to select the folder containing your `.csv` graph files.  
2. Use the **Sub-graph selector** to choose one or multiple graph layers.  
3. Adjust the **layout** and **metrics** to explore structural properties.  
4. Optionally apply a **graph cut** for better readability on large graphs.  
5. Switch between **Graph**, **Histogram**, and **Animation** views for different insights.
---
## ✨ Main Functionalities

### 🔹 Data Loading & Settings
- Load directories containing graph files (`.csv` format).
- Select one or multiple graph layers for analysis.
- Access a **Settings panel** to configure visualization parameters.
- Reset options to default values.
- Integrated help/documentation link.

---

### 🔹 Graph Visualization
- Display graphs in **2D or 3D layouts**.
- Multiple **graph layout algorithms** available:
  - Circle, Force-directed (FR), Kamada-Kawai (KK), Random, Tree, and more.
- Show or hide node labels.
- Adjust **edge thickness** and **node size**.
- Customize **edge and node color maps**.

---

### 🔹 Node & Edge Metrics
- Compute and visualize node-level metrics:
  - Strength  
  - Betweenness  
  - Closeness  
  - Eigenvector Centrality  
  - PageRank  
  - Hub Score  
  - Authority Score  
  - Rich-Club  
  - K-Core
- Visualize edge weights using color scales.

---

### 🔹 Graph Filtering (Graph-Cut)
- Apply different **graph-cut strategies** to prune edges:
  - **Threshold cut**: Remove edges below a chosen weight threshold.
  - **Mutual Nearest Neighbors (MNN)**: Keep edges only between mutual nearest neighbors.
  - **Nearest Neighbors (NN)**: Keep edges to the closest nodes (not necessarily mutual).
- Parameter values can be set interactively through pop-up dialogs.

---

### 🔹 Clustering & Community Detection
- Detect communities in graphs using the **Louvain algorithm**.
- Automatically color nodes by detected clusters.

---

### 🔹 Multiple Display Modes
Switch between three main result displays:
1. **Graph(s)** – Visual representation of the selected graph layers.  
2. **Histogram** – Statistical analysis of node/edge metrics.  
3. **Animation** – Dynamic visualization of graph evolution with adjustable animation speed.

---

## 📊 Applications
- Comparative analysis of multilayer networks.  
- Community detection and visualization.  
- Exploring structural properties with customizable layouts and metrics.  
- Animated graph evolution for temporal/multilayer data.

---

## 📌 Notes
- Current version supports **CSV-formatted graph files** only.  
- Future updates may expand compatibility and add new metrics.  
