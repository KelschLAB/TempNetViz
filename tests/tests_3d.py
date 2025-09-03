import unittest
import sys, os
import matplotlib.pyplot as plt
sys.path.append("..\\src")

if __name__ == "__main__" and __package__ is None:
    # Go up one level to the package root
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    __package__ = "tempgraphviz"

from tempgraphviz.read_graph import *
from tempgraphviz.settings_window import settingsWindow
from tempgraphviz.listbox_selection import MultiSelectDropdown
from tempgraphviz.tooltip import ToolTip
from tempgraphviz.temporal_layout import plot_temporal_layout

test_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(test_dir, os.pardir))
path = os.path.join(project_root, "data", "nosemaze", "both_cohorts_3days", "G1\\")

file1 = "approaches_resD3_1.csv"
file2 = "approaches_resD3_2.csv"
file3 = "approaches_resD3_3.csv"
file4 = "interactions_resD3_2.csv"

data = read_graph([path+file1], mnn = 3, return_ig=False)[0]
if isSymmetric(data):
    g = ig.Graph.Weighted_Adjacency(data, mode='undirected')
else:
    g = ig.Graph.Weighted_Adjacency(data, mode='directed')

class Test3D(unittest.TestCase):         
    ## Test different keyword arguments in multi-layer case
    def test_default_3d(self):
        """Tests multilayer graph with 'k-core' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                          node_metric = "none", mutual = True, idx = [], node_size = 5, edge_width = 2,
                          scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                          node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....") 
            
    def test_betweenness_3d(self):
        """Tests multilayer graph with 'betweenness' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                          node_metric = "betweenness", mutual = True, idx = [], node_size = 5, edge_width = 2,
                          scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                          node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)            
            plt.close(fig)
        except:
            self.fail("....") 

    def test_kcore_3d(self):
        """Tests multilayer graph with 'k-core' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "k-core", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_rc_3d(self):
        """Tests multilayer graph with 'rich-club' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "rich-club", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")
        
    def test_pagerank_3d(self):
        """Tests multilayer graph with 'page rank' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "pagerank", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_hubscore_3d(self):
        """Tests multilayer graph with 'hub score' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "hub score", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_evcentrality_3d(self):
        """Tests multilayer graph with 'eigenvector centrality' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "eigenvector centrality", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")          
            
    def test_authority_3d(self):
        """Tests multilayer graph with 'authority score' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "authority", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")      
        
    def test_closeness_3d(self):
        """Tests multilayer graph with 'closeness' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = None, deg = 2, 
                 node_metric = "closeness", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")  
            
    def test_strength_3d(self):
        """Tests multilayer graph with 'strength' metric works"""
        try:
            fig = plt.Figure()
            ax = fig.add_subplot(111, projection='3d')
            display_graph([path+file4, path+file3], ax, mnn = 4, deg = 2, 
                 node_metric = "strength", mutual = True, idx = [], node_size = 5, edge_width = 2,
                 scale_edge_width = True, between_layer_edges = False, cluster_num = None, rm_index = True,
                 node_labels = False, show_planes = True, edge_cmap = cm.Greys, node_cmap = cm.Greens)
            plt.close(fig)
        except:
            self.fail("....")  
            

if __name__ == '__main__':
    unittest.main()