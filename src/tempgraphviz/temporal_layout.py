import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
import os, sys
if __name__ == "__main__" and __package__ is None:
    # Go up one level to the package root
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    __package__ = "tempgraphviz"
from .read_graph import *


def plot_temporal_layout(path_to_file, ax=None, percentage_threshold = 0.0, mnn = None, avg_graph = False,
                  affinity = True, rm_fb_loops = True, mutual = True, rm_index = True, **kwargs):
    
    if rm_index == False and ("node_labels" in kwargs and kwargs["node_labels"]):
        node_labels = [str(i) for i in range(len(read_labels(path_to_file)))] 
    elif ("node_labels" in kwargs and kwargs["node_labels"]):
        node_labels = read_labels(path_to_file) 
    else:
        node_labels = None
        
    layers = read_graph(path_to_file, percentage_threshold = percentage_threshold, mnn = mnn, mutual = mutual, \
                      avg_graph = avg_graph, affinity = affinity, rm_fb_loops = rm_fb_loops, rm_index = rm_index, return_ig=True)

    data = read_graph(path_to_file, percentage_threshold = percentage_threshold, mnn = mnn, mutual = mutual, \
                      avg_graph = avg_graph, affinity = affinity, rm_fb_loops = rm_fb_loops, rm_index = rm_index)[0]

    if isSymmetric(data):
        directed = False
    else:
        directed = True
        
    default_node_size = kwargs["node_size"] if "node_size" in kwargs else 15
    default_edge_width = kwargs["edge_width"] if "edge_width" in kwargs else 5
        
    g = ig.Graph.Tree(data.shape[0], 2) 
    timesteps = len(layers)
    g.vs["name"] = node_labels
    
   
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    events = [g.get_edgelist() for g in layers]
    
    
    # Plot each time point
    for time_idx in range(timesteps):
        layout = []
        for i in range(data.shape[0]):  # 5 nodes
            layout.append((time_idx, data.shape[0]-i))  # Position nodes vertically (y-axis)
        
        # ax = axes[time_idx]        
        # Create a subgraph for this time point
        # In a real scenario, you would have different edges at different times
        subgraph_edges = events[time_idx]
        subgraph = ig.Graph(data.shape[0], edges=subgraph_edges,  directed = directed)
        
        # Visual styling
        visual_style = {}
        # visual_style["vertex_label"] = g.vs["name"]
        visual_style["vertex_size"] = 30
        visual_style["vertex_color"] = "black"
        visual_style["vertex_label_size"] = 10
        visual_style["edge_width"] = 2
        visual_style["edge_color"] = "gray"
        # visual_style["bbox"] = (200, 300)
        # visual_style["margin"] = 50
        visual_style["edge_curved"] = 0.5
        visual_style["edge_arrow_width"] = 10 if directed else 0
        if "edge_cmap" in kwargs:
            edge_cmap = kwargs["edge_cmap"]
        else:
            edge_cmap = get_cmap('Greys')
        
        if "scale_edge_width" in kwargs and type(kwargs["scale_edge_width"]) == bool:
            if kwargs["scale_edge_width"]: #if true, adapt edge_thickness to edge value, else all edges are shown with same width.
                display_edge_width = rescale(np.array([w['weight'] for w in layers[time_idx].es]), default_edge_width)
                edge_color = [edge_cmap(edge) for edge in rescale(np.array([w['weight'] for w in layers[time_idx].es])) - 0.01]
            else:
                display_edge_width = np.array([0.99 if w['weight'] > 0.01 else 0 for w in layers[time_idx].es])*default_edge_width
                edge_color = [edge_cmap(edge) for edge in rescale(np.array([w['weight'] for w in layers[time_idx].es])) - 0.01]
        else:
            display_edge_width = rescale(np.array([w['weight'] for w in layers[time_idx].es]), default_edge_width)
            edge_color = [edge_cmap(edge) for edge in rescale(np.array([w['weight'] for w in layers[time_idx].es])) - 0.01]

        visual_style["edge_width"] = display_edge_width
        visual_style["edge_color"] = edge_color
        ig.plot(subgraph, target=ax, layout=layout, **visual_style)
    
    # Set proper x-axis labels and limits
    ax.set_xlim(-0.5, timesteps - 0.5)  # Add some padding
    ax.set_xticks(range(timesteps))  # Set ticks at each time step position
    ax.set_xticklabels([f'{i+1}' for i in range(timesteps)])  # Label each tick
    ax.set_xlabel('Timesteps')
    plt.tight_layout()
    plt.show()
    
path = "..\\..\\data\\nosemaze\\both_cohorts_1days\\G1\\"
file1 = "interactions_resD1_01.csv"
file2 = "interactions_resD1_02.csv"
file3 = "interactions_resD1_03.csv"
file4 = "interactions_resD1_04.csv"
file5 = "interactions_resD1_05.csv"
file6 = "interactions_resD1_06.csv"
file7 = "interactions_resD1_07.csv"
file8 = "interactions_resD1_08.csv"
file9 = "interactions_resD1_09.csv"
file10 = "interactions_resD1_10.csv"
file11 = "interactions_resD1_11.csv"
file12 = "interactions_resD1_12.csv"
paths = [path+file1, path+file2,path+file3, path+file4, 
        path+file5,  path+file6,  path+file7, path+file8
        , path+file9, path+file10, path+file11, path+file12]

plot_temporal_layout(paths, mnn = 5, scale_edge_width = True, node_size = 10, edge_width = 2, between_layer_edges = False, rm_fb_loops=True,  cluster_num = None, node_labels = True, rm_index = True,
node_cmap = cm.coolwarm, edge_cmap = cm.Greys)