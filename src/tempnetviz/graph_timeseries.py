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
    
from read_graph import *
import pandas as pd
import time 
import matplotlib.colors as mcolors
    
def display_graph_timeseries(path_to_file, ax, percentage_threshold = 0.0, mnn = None, affinity = True,
                     rm_fb_loops = True, mutual = True, rm_index = True, node_metric = "strength"):
    """
    This function displays the temporal graph to analyze as a timeseries, where each node is represented by
    the evolution of its metric values as a function of time

    Parameters
    ----------
    path_to_file : string
        path specifying where the file containing the matrix representing the graph 
        is stored. Should be a .csv file.
    ax : matplotlib.axis
        the axis to plot the graph onto.
    threshold : parameter specifying the edge value threshold under which edges are not displayed.
    mnn : number of nearest neighbours for graph cut
    affinity: Whether the edges represent an affinity measurement (if True) or a distance (if False) (i.e. high value = high similarity or 
        high value = high difference). Defaults to True.
    rm_fb_loops: Bool. Whether or not to remove feedback loops from graph display
    **kwargs : strings
        layout : specifies which layout to use for displaying the graph. see igraph documentation for 
            a detailed list of all layout. should be given as a string as stated in the igraph doc.
        node_metric : specifies which metric to use in order to color and size the vertices of the graph.
            allowed values: ["strength", "betweenness", "closeness", "eigenvector centrality", "page rank", "hub score", "authority score"]

    Returns
    -------
    None.

    """

    # for igrpah based metrics
    layers = read_graph(path_to_file, percentage_threshold = percentage_threshold, mnn = mnn, return_ig=True, affinity = affinity,
                        rm_fb_loops = rm_fb_loops, mutual = mutual, rm_index = rm_index) 
    # rc and kcores are computed from numpy arrays
    layers_data = read_graph(path_to_file, percentage_threshold = percentage_threshold, mnn = mnn, return_ig=False,
                             affinity = affinity, rm_fb_loops = rm_fb_loops, mutual = mutual, rm_index = rm_index)

    default_node_size = 1 
    if kwargs["node_metric"] == "none":
        return
            
    elif kwargs["node_metric"] == "betweenness":
        node_size = []
        for g in layers:
            edge_betweenness = g.betweenness(weights = [1/(e['weight']) for e in g.es()]) #taking the inverse of edge values as we want high score to represent low distances
            edge_betweenness = ig.rescale(edge_betweenness)
            node_size.append(np.array(edge_betweenness)*default_node_size+0.07)
            
    elif kwargs["node_metric"] == "strength":
        node_size = []
        for g in layers:
            edge_strength = g.strength(weights = [e['weight'] for e in g.es()])
            edge_strength = ig.rescale(edge_strength)
            node_size.append(np.array(edge_strength)*default_node_size+0.07)
    elif kwargs["node_metric"] == "closeness":
        node_size = []
        for g in layers:
            edge_closeness = g.closeness(weights = [1/(e['weight']) for e in g.es()]) #taking the inverse of edge values as we want high score to represent low distances
            edge_closeness = ig.rescale(edge_closeness)
            node_size.append(np.array(edge_closeness)*default_node_size+0.07)
    elif kwargs["node_metric"] == "hub score":
        node_size = []
        for g in layers:
            edge_hub = g.hub_score(weights = [e['weight'] for e in g.es()])
            edge_hub = ig.rescale(edge_hub)
            node_size.append(np.array(edge_hub)*default_node_size+0.07)
    elif kwargs["node_metric"] == "authority score":
        node_size = []
        for g in layers:
            edge_authority = g.authority_score(weights = [e['weight'] for e in g.es()])
            edge_authority = ig.rescale(edge_authority)
            node_size.append(np.array(edge_authority)*default_node_size+0.07)
    elif kwargs["node_metric"] == "eigenvector centrality":
        node_size = []
        for g in layers:
            edge_evc = g.eigenvector_centrality(weights = [e['weight'] for e in g.es()])
            edge_evc = ig.rescale(edge_evc)
            node_size.append(np.array(edge_evc)*default_node_size+0.07)
    elif kwargs["node_metric"] == "page rank":
        node_size = []
        for g in layers:
            edge_pagerank = g.personalized_pagerank(weights = [e['weight'] for e in g.es()])
            edge_pagerank = ig.rescale(edge_pagerank)
            node_size.append(np.array(edge_pagerank)*default_node_size+0.07)
    elif kwargs["node_metric"] == "rich-club":
        node_size = []
        for g in layers:
            k_degree = kwargs["deg"]
            size = rich_club_weights(g, k_degree, 0.01)
            node_size.append(np.array([n*default_node_size for n in size]))
    elif kwargs["node_metric"] == "k-core":
        node_size = []
        for d in layers_data:
            k_degree = kwargs["deg"]
            size = k_core_weights(d, k_degree, 0.01)
            node_size.append(np.array([n*default_node_size for n in size]))
            
    node_size = np.array(node_size)
    
        

if __name__ == '__main__':

    path = "..\\..\\data\\nosemaze\\both_cohorts_1days\\G10\\"
    file1 = "interactions_resD1_01.csv"
    file2 = "interactions_resD1_02.csv"
    file3 = "interactions_resD1_03.csv"
    file4 = "interactions_resD1_04.csv"
    file5 = "interactions_resD1_05.csv"

    f = plt.Figure()
    fig, ax = plt.subplots(1, 1)
    display_graph_timeseries([path+file1, path+file2, path+file3, path+file4, path+file5], ax, mnn = None, deg = 3, percentage_threshold = 0,
                  node_metric = "strength", mutual = True, idx = [], node_size = 5, edge_width = 2, layout = "circle",
                  scale_edge_width = True, between_layer_edges = False,  cluster_num = None, rm_index = True,
                  node_labels = True, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.coolwarm)
    plt.show()




