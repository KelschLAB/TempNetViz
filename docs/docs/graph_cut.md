# Graph Cut
When working with large graphs, a direct representation of every single link can quickly become overcrowded.
In such cases, graph pruning can help improve visibility while preserving the essential features in the data. 
TempGraphViz offers several ways to do this, available with the **```graph cut```** button. Graph cuts are used to simplify the network by **removing weak** or **irrelevant edges**, making patterns easier to analyze and visualize.
Below is a list of the available cut or pruning methods available.
---


### Threshold Cut  
Removes the weakest connections in the graph. You choose a **percentage** (relative to the strongest connection), and all edges below this level are hidden.  

- **Example:** If the strongest connection has weight 100, and you set the threshold to 10%, then all edges weaker than 10 are removed.  
- **Best for:** filtering out background noise while keeping dominant patterns visible.  

---

### Nearest Neighbors Cut (NN Cut)  
For each node, only its top k **strongest connections** are kept. You decide how many neighbors should remain connected (e.g., k = 2 or 3...).  

- Each node stays connected to a limited number of its closest partners.  
- **Best for:** focusing on **local structures** around each node and avoiding clutter from weak links.  

---

### Mutual Nearest Neighbors Cut (MNN Cut)  
A stricter version of NN Cut. Here, a connection between two nodes is kept **only if both nodes rank each other among their top neighbors**.  

- Creates a much sparser graph, highlighting only the most **reciprocal and reliable relationships**.  
- **Best for:** revealing **core structures** and strongly linked communities.  

---


## Quick Guide: Which Cut to Choose?  

| Method           | What it shows best            | Use it when… |
|------------------|-------------------------------|--------------|
| **Threshold Cut** | Strong connections vs. weak noise | You want to filter out background clutter |
| **NN Cut**       | Local neighborhoods           | You want each node to show its closest relationships |
| **MNN Cut**      | Reciprocal strong links       | You want to see the **most reliable and symmetric** structures |  

---
