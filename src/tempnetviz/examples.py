import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import igraph as ig
from copy import deepcopy
from matplotlib.cm import ScalarMappable, get_cmap
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, Normalize
from igraph.drawing.colors import ClusterColoringPalette
import random
import os, sys
from copy import copy
from warnings import warn
from tkinter import messagebox as mb

if __name__ == "__main__" and __package__ is None:
    # Go up one level to the package root
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    __package__ = "tempnetviz"
    
from .graph_animation import *
from .temporal_layout import *
from .read_graph import *
import pandas as pd
import time 
import matplotlib.colors as mcolors

if __name__ == "__main__":
    path = "..\\..\\data\\nosemaze\\both_cohorts_1days\\G10\\"
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
    file13 = "interactions_resD1_13.csv"
    file14 = "interactions_resD1_14.csv"

## Graph display
    # Averaged graph: calling the 'display_graph' function with avg_graph = True as argument    
    f = plt.Figure()
    fig, ax = plt.subplots(1, 1)
    display_graph([path+file1, path+file2, path+file3, path+file4, path+file5], ax, mnn = None, deg = 0, percentage_threshold = 0,
                  node_metric = "none", mutual = True, idx = [], node_size = 5, edge_width = 2, avg_graph = True,
                  scale_edge_width = True, between_layer_edges = False, rm_index = True,
                  node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
    plt.title("Averaged graph over 5 days")
    plt.show()
    
    # Stacked plot example. To apply a graph cut, change 'mnn' to an integer > 1
    f = plt.Figure()
    fig, ax = plt.subplots(1, 1)
    ax = fig.add_subplot(111, projection='3d')
    display_graph([path+file1, path+file2, path+file3, path+file4, path+file5], ax, mnn = None, deg = 3, percentage_threshold = 0,
                  node_metric = "none", mutual = True, idx = [], node_size = 5, edge_width = 2, show_planes = True,
                  scale_edge_width = True, between_layer_edges = True, rm_index = True)
    plt.title("Stacked view of 5 experimental days")
    plt.show()
    
## Histograms
    # Stacked histogram plot example, via Stacked = True  
    f = plt.Figure()
    fig, ax = plt.subplots(1, 1)
    display_stats([path+file1, path+file2, path+file3, path+file4, path+file5], ax, mnn = None, deg = 3, percentage_threshold = 0,
                  node_metric = "strength", mutual = True, idx = [], node_size = 5, edge_width = 2, bins = 5,
                  scale_edge_width = True, between_layer_edges = False, rm_index = True, show_planes = True, show_legend = False)
    plt.title("Strength histogram\n color codes for time (in days)")
    plt.show()
    
    # Side by side histogram plot example, using Stacked = false  
    f = plt.Figure()
    fig, ax = plt.subplots(1, 1)
    display_stats([path+file1, path+file2, path+file3, path+file4, path+file5], ax, mnn = None, deg = 3, percentage_threshold = 0,
                  node_metric = "strength", mutual = True, idx = [], node_size = 5, edge_width = 2, bins = 5, stacked = False,
                  scale_edge_width = True, between_layer_edges = False, rm_index = True, show_planes = True, show_legend = False)
    plt.title("Strength histogram\n color codes for time (in days)")
    plt.show()

## Temporal layout example
    paths = [path+file1, path+file2,path+file3, path+file4, 
            path+file5,  path+file6,  path+file7]
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    plot_temporal_layout(paths, ax, mnn = 5, deg = 3,
                         node_size = 15, edge_width = 5, between_layer_edges = False, 
                         rm_fb_loops=True, node_labels = False, rm_index = True,
                         node_metric = "strength", node_cmap = cm.coolwarm, edge_cmap = cm.coolwarm, scale_edge_width = True)
    plt.title("Temporal layout over 7 experimental days")
    plt.show()
    
## animation example  
    files = [path+file1, path+file2, path+file3, path+file4, path+file5, path+file6, path+file7, path+file8, path+file9, path+file10,
             path+file11, path+file12, path+file13, path+file14]
    anim = display_animation(files, root = None, mnn = None, deg = 0, 
                      percentage_threshold = 0, layout = "circle",
                  node_metric = "strength", mutual = True, idx = [], node_size = 40, edge_width = 2,
                  scale_edge_width = False, between_layer_edges = False, node_labels = True, rm_index = True,
                  node_cmap = cm.Grays, edge_cmap = cm.Grays)
    # anim.save(r"path_to_save\interactions.gif", writer="pillow", fps=2)
    
    
## community clustering example. The indices provided by this can be passed to other plotting functions for display
    data = read_graph([path+file1], mnn = 3, return_ig=False)[0]
    if isSymmetric(data):
        g = ig.Graph.Weighted_Adjacency(data, mode='undirected')
    else:
        g = ig.Graph.Weighted_Adjacency(data, mode='directed')
    c = community_clustering([path+file1, path+file2, path+file3, path+file4], algorithm = "infomap", mnn = 4, mutual = True, affinity = True)
    print(c)
    
## Example of rich club analysis, with graph cut of mnn = 3 and degree = 3
    datapath = "..\\..\\data\\nosemaze\\both_cohorts_3days\\G1\\"
    fig, axs = plt.subplots(5, 1, figsize=(4, 8)) #putting all results directly on same figure
    for i in range(5):
        file = "interactions_resD3_"+str(i+1)+".csv"
        display_graph([datapath+file], axs[i], mnn = 3, node_metric = "rich-club", deg = 3, mutual = True,
                          layout = "circle", node_size = 12, node_labels = None, edge_width = 1.5, scale_edge_width = False)

    axs[0].set_title("Rich-club (RC) analysis:\nEach graph represent an experimental day,\nBold nodes are part of RC\nSome nodes are consistently part of RC")
    # axs[0].set_title(labels[graph_idx]+", total interactions: "+str(total), fontsize=16)
    plt.show()
    