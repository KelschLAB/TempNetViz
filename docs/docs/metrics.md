# Node and Graph Metrics

To help visualize potential relevant structure or important nodes in the data, TempGraphViz provides the possibility to compute several **metrics**.
These metrics determine how nodes are **sized**, **colored**, and how statistics are displayed.

---

## Available Metrics

| Metric | Description |
|--------|-------------|
| **None** | No node-specific metric is applied. The graph displays **raw edge weights** only. |
| **Strength** | The sum of edge weights connected to a node. A higher strength means the node has stronger or more numerous connections. |
| **Betweenness** | Measures how often a node appears on the shortest paths between other nodes. Nodes with high betweenness act as important **bridges** in the network. |
| **Closeness** | Reflects how close a node is to all other nodes in the network. Nodes with high closeness can reach others quickly (shorter average path length). |
| **Eigenvector Centrality** | Measures a node’s influence based on the idea that connections to **important nodes** contribute more than connections to less important ones. |
| **PageRank** | A variant of eigenvector centrality. It gives higher scores to nodes connected to other highly connected nodes. Originally developed for ranking webpages. |
| **Hub Score** | In the **HITS algorithm**, hubs are nodes that point to many authoritative nodes. A high hub score means the node is a good “information provider.” |
| **Authority Score** | The complement of the hub score in the **HITS algorithm**. A node has a high authority score if many hubs point to it, making it an important “information source.” |
| **Rich-Club** | Identifies a subset of nodes (the “rich club”) that are **highly connected among themselves**. The parameter `k` controls the minimum degree for inclusion. Nodes outside the club are down-weighted. |
| **K-Core** | Identifies the largest subgraph where every node has at least `k` connections within the group. Useful for finding **tightly knit groups**. |

---

## Notes

- For **Rich-Club** and **K-Core**, you must specify a degree parameter `k`.  
- Metrics affect how nodes are displayed:  
  - **Size** → proportional to the metric value.  
  - **Color** → mapped via the selected colormap.  
- In histogram mode, metrics determine the values plotted.  
- When **None** is selected, histograms display **edge weights** directly.  

