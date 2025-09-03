import unittest
import sys, os
import matplotlib.pyplot as plt
sys.path.append("..")

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

class Test1D(unittest.TestCase):
    
    ## Test different keyword arguments in single layer case
    def test_default(self):
        """Tests displaying of graph with 'k-core' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "none", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....") 
            
    def test_betweenness(self):
        """Tests displaying of graph with 'betweenness' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "betweenness", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....") 

    def test_kcore(self):
        """Tests displaying of graph with 'k-core' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "k-core", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_rc(self):
        """Tests displaying of graph with 'rich-club' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "rich-club", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")
        
    def test_pagerank(self):
        """Tests displaying of graph with 'page rank' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "page rank", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_hubscore(self):
        """Tests displaying of graph with 'hub score' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "hub score", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")
            
    def test_evcentrality(self):
        """Tests displaying of graph with 'eigenvector centrality' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "eigenvector centrality", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")          
            
    def test_authority(self):
        """Tests displaying of graph with 'authority score' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "authority score", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")      
        
    def test_closeness(self):
        """Tests displaying of graph with 'closeness' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            # no graph cut, as it is incompatible with closeness
            display_graph([path+file4], ax, mnn = None, deg = 2, node_metric = "closeness", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")  
            
    def test_strength(self):
        """Tests displaying of graph with 'strength' metric works"""
        try:
            fig, ax = plt.subplots(1, 1)
            display_graph([path+file4], ax, mnn = 4, deg = 2, node_metric = "strength", mutual = True, idx = [], cluster_num = None)
            plt.close(fig)
        except:
            self.fail("....")  
            

if __name__ == '__main__':
    unittest.main()