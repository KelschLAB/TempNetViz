---
title: 'TempNetViz: a GUI for temporal graphs visualization'
tags:
  - Python
  - Temporal graphs
authors:
  - name: Corentin Nelias
    orcid: 0000-0001-6266-5575
    affiliation: 1

affiliations:
 - name: Corentin Nelias, Unimedizin Mainz, Germany
   index: 1


bibliography: paper.bib
---

# Summary
Temporal network analysis is an emerging and rapidly expanding research area concerned with the study of how graphs evolve over time. 
Graphs provide a natural representation of complex systems and have therefore become indispensable across a wide range of scientific domains, including neuroscience, biology, sociology, and natural language processing. 
While traditional network analysis has focused primarily on static structures, most real-world systems are inherently dynamic: their connectivity patterns change, sometimes subtly and sometimes dramatically, over time. 
As a result, understanding both the structural properties of a network and their temporal evolution is essential for uncovering the mechanisms that drive system behavior.

Temporal network analysis addresses this need by jointly examining topology and dynamics, thereby enabling researchers to capture the interplay between stable structural features and transient temporal variations. 
The field is intrinsically multidisciplinary, drawing upon diverse methodologies from graph theory, dynamical systems, statistics, and machine learning. 

This methodological diversity, can pose significant challenges for researchers, particularly at the stage of initial data exploration.
In this context, effective visualization is needed to provide an intuitive entry point into the data and help guide subsequent analytical decisions. 
To this aim, we developped TempNetViz to visualize temporal network data, support early-stage exploration and highlight potential structural and temporal patterns. Particular attention was given to ease of usability, to make data exploration as intuitive as possible.
TempNetViz was build using igraph and networkx, two of the most popular graph visualization packages in Python [CITE] [CITE].

# Statement of need
There are, To the best of our knowledge, no available graphical user interfaces (GUIs) designed specifically for the interactive visualization of temporal graphs. 
Although some established graph visualization GUIs provide ways for displaying temporal networks [CITE] [CITE], they were not tailored for this purpose. The available features are therefore limited and rely on specialized internal data formats or external plugins. 
This represents a substantial learning barrier that must be overcome before any analysis can be conducted. Moreover, it makes systematic comparison across different data representations impossible.

While numerous Python packages for temporal graph analysis are available [CITE][CITE][CITE], they either offer limited visualization capabilities or are more oriented towards modeling and classification. 
Leveraging the strength of the existing dependencies also requires some coding expertise, which can represent a significant obstacle for researchers lacking extensive programming experience. 
To address these limitations, we developed, we developped TempNetViz to provide and accessible and user-friendly way to visualize temporal graphs.

# Key features
Showcase the key features of the GUI

# Related software
cite existing softwares and GUI for graph visualization
 [@igraph] 

# Research application
Cite sRC paper here, and show how we can observe the sRC with the GUI.
Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from ...

# References

igraph 

networkx

Bastian, M., Heymann, S., & Jacomy, M. (2009, March). Gephi: an open source software for exploring and manipulating networks. In Proceedings of the international AAAI conference on web and social media (Vol. 3, No. 1, pp. 361-362).

Cytoscape + Timenexus




# previous version:

Temporal network analysis is a growing area of research focused on understanding how graphs evolve over time. Graphs can be used to represent a broad variety of systems, and are thus commmonly used in wide array of scientific fields such as neuroscience, biology, sociology and natural language processing. 
However, most systems under study are not static, and just as the structure of a graph can be of key importance, so can its time evolution. Temporal network analysis aims to study both structure and time variation simulatneously, in order to understand the interplay between these fundamental aspects.
As an inherently multidisciplinary field, it draws on diverse methodologies, multiple mathematical frameworks and data representation. This diversity can make initial exploration and comparison difficult due to the absence of standardized conventions.
In this context, effective visualization is needed to provide an intuitive entry point into the data and help guide subsequent analytical decisions. To this aim, we developped TempNetViz to visualize temporal betwork data, support early-stage exploration and highlight potential structural and temporal patterns.
