import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

# Create a temporal graph example
g = ig.Graph.Tree(5, 2)  # Create a simple tree graph with 5 nodes

# Set node names according to your example
g.vs["name"] = ["Eliot", "Dylan", "Casey", "Blake", "Ashley"]

# Create a custom layout for temporal visualization
# We'll position nodes vertically and time events horizontally
layout = []
for i in range(5):  # 5 nodes
    layout.append((0, 4-i))  # Position nodes vertically (y-axis)

# Create a figure with subplots for each time point
fig, axes = plt.subplots(1, 20, figsize=(12, 6))
fig.suptitle('Temporal Network')

# Define events at different time points (simplified example)
events = [
    [0, 1],  # Time 1: Eliot connected to Dylan
    [1, 2],  # Time 2: Dylan connected to Casey
    [2, 3],  # Time 3: Casey connected to Blake
    [3, 4],  # Time 4: Blake connected to Ashley
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [1, 2],  # Time 2: Dylan connected to Casey
    [2, 3],  # Time 3: Casey connected to Blake
    [3, 4],  # Time 4: Blake connected to Ashley
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
    [0, 1],  # Time 1: Eliot connected to Dylan
]

# Plot each time point
for time_idx in range(20):
    ax = axes[time_idx]
    ax.set_xlabel(f'{time_idx+1}')
    
    # Create a subgraph for this time point
    # In a real scenario, you would have different edges at different times
    subgraph_edges = events[time_idx]
    subgraph = ig.Graph(5, edges=[subgraph_edges])
    
    # Visual styling
    visual_style = {}
    # visual_style["vertex_label"] = g.vs["name"]
    visual_style["vertex_size"] = 30
    visual_style["vertex_color"] = "lightblue"
    visual_style["vertex_label_size"] = 10
    visual_style["edge_width"] = 2
    visual_style["edge_color"] = "gray"
    visual_style["bbox"] = (200, 300)
    visual_style["margin"] = 50
    
    # Plot this time point
    ig.plot(subgraph, target=ax, layout=layout, **visual_style)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 5)
fig.set_xlabel("time")

plt.tight_layout()
plt.show()