# mrSina
A project !

Multilayer Network Analysis

Introduction

This repository is designed for analyzing and visualizing multilayer networks. It supports a range of functionalities from data preprocessing to complex network analysis and visualization.
Installation

To install the required dependencies for this project, it is strongly recommended to create a virtual environment using venv. Once you have navigated to the root directory of the project, you can establish the environment by executing the following command:

    python3 -m venv .graph

And Activate it :

    source .graph/bin/activate

then you can run the command below to install the dependencies :

    pip install -r requirements.txt

This will install all the required Python packages as listed in the requirements.txt file.

* Structure

    Archive/: Contains historical data and figures for reference.
    docs/: Documentation and manuscripts related to the project.
    input/: Input data files for processing.
    main/: Core Python scripts and modules for the project.
    output/: Generated output, including processed data and figures.
    Rside/: R scripts for data preprocessing.
    scripts/: Additional utility scripts.

* Key files:

    index.ipynb: Jupyter notebook demonstrating example usages of the library.
    .gitignore: Specifies files and directories to be ignored by version control.
    LICENSE: The full text of the license governing this project.
    README.md: An overview of the project for users and contributors.
    requirements.txt: Lists all the dependencies for the project.

Usage

The project is primarily used through Jupyter notebooks, such as index.ipynb. Open this notebook in a Jupyter environment:

    jupyter notebook index.ipynb

Data

Data files are stored in input/ and are processed by scripts in Rside/. The R scripts like link_dataPrepare.R are used to prepare the data for analysis.

Output

The output from analyses and scripts will be located in the output/ directory. This includes CSV files and visualizations in various formats.


# DataHandle Class Documentation

Introduction

The DataHandle class is part of a Python module that facilitates the handling and manipulation of network data for multilayer network analysis. This class provides methods for initializing data, identifying key attributes, and modifying network links based on node classifications.
Class Definition


    class DataHandle:
        def __init__(self,
                     data_links: dict, 
                     data_nodes: dict, 
                    layer_one_name:str='Advertisers', 
                    layer_two_name:str='Publishers'):
        # Initialization and instance variables setup

Initialization

The *__init__* method initializes the DataHandle object with dictionaries representing the links and nodes of a network, as well as optional names for two types of network layers.

* Parameters:

    data_links: A dictionary containing the edge data.
    data_nodes: A dictionary containing the node data.
    layer_one_name: The name for the first layer of nodes (default is 'Advertisers').
    layer_two_name: The name for the second layer of nodes (default is 'Publishers').

Method: *initial_keys*

    This method processes the keys from the node and link data to identify relevant attributes such as node IDs and colors, and classifies nodes into two categories based on their names.
* Parameters:

    node_id_label: The label to identify node IDs within the data (optional).
    color_label: The label to identify node colors within the data (optional).

* Returns:

    Sets internal attributes used to identify node and edge properties.

Method: *initial_data*

Prepares the data by using key labels to classify nodes and validate the structure of the network data.
* Parameters:

    edge_labels: A tuple containing the labels for the source and target nodes in the links data.
    node_id_label: The label for node IDs.
    advertiser_nodes: A list of nodes identified as advertisers.
    publisher_nodes: A list of nodes identified as publishers.
    color_label: The label for node colors.

* Returns:

    Throws KeyError if labels are missing.
    Throws ValueError if nodes lists are not provided or are not lists.

Method: *modify_links*

Reclassifies the links into categories based on the node types they connect (i.e., within layer one, within layer two, or interconnecting).
* Parameters:

    len_of_sources_and_targets: The number of source-target pairs (optional).
    sources: A list of source nodes (optional).
    targets: A list of target nodes (optional).

* Returns:

    A tuple containing three lists: layer_one_links, layer_two_links, interconnected_links.


*Notes*

    Ensure that the node and link data passed to the class constructor follow the expected format.
    Proper exception handling has been implemented to guide the correct usage of methods.


# Graph Class Documentation

Introduction

The Graph class encapsulates functionalities for constructing, modifying, and visualizing single-layer and multilayer network graphs. It provides an interface for handling network data, adding nodes and links, and generating visual representations of the network structure.

Class Definition


    class Graph:
        def __init__(self, 
                     layer_one_name: str, 
                     layer_two_name: str):
        # Initialization and instance variables setup

Initialization

The *__init__* method sets up a Graph instance with names for two distinct layers within the network.

* Parameters:

    layer_one_name: The name identifier for the first layer in the network.
    layer_two_name: The name identifier for the second layer in the network.

Method: *create*

Initializes a new graph object either as a NetworkX graph or a MultilayerNetwork object.
* Parameters:

    Aspects: The number of aspects for a MultilayerNetwork (default is 1).
    fully_Interconnect: Boolean indicating whether layers should be fully interconnected in a MultilayerNetwork (default is False).
    of_type_nx: Boolean indicating whether to create a NetworkX graph instead of a MultilayerNetwork (default is False).

* Returns:

    A NetworkX graph or a MultilayerNetwork object.

Method: *add_node*

Adds nodes to a NetworkX graph. Not applicable for MultilayerNetwork graphs, as nodes are added with the add_links method.
* Parameters:

    nodes_to_add: A list of node identifiers to add to the graph.
    nx_use: Boolean flag indicating the use of NetworkX (default is True).
    G: An existing NetworkX graph object to which nodes will be added.

* Returns:

    A NetworkX graph with the new nodes added.

Method: *add_links*

Adds edges to the graph based on the specified links for each layer and the interconnections.
* Parameters:

    layer_one_links: A list of edges within the first layer.
    layer_two_links: A list of edges within the second layer.
    Interconnected_links: A list of edges that interconnect the two layers.
    nx_use: Boolean flag indicating the use of NetworkX (default is False).
    G: An existing graph object to which edges will be added.

* Returns:

    A tuple of NetworkX graph objects representing the two layers and their interconnections if nx_use is True; otherwise, a MultilayerNetwork graph.

Method: *show*

Visualizes the graph using the specified layout parameters.
* Parameters:

    G: The graph object to visualize.
    return_Graph_object: Boolean indicating whether to return the graph object after visualization (default is False).

* Returns:

    The graph object if return_Graph_object is True; otherwise, None.

*Notes*

    For MultilayerNetwork objects, the layers and nodes are added in tandem with the links.
    NetworkX functionality within this class primarily supports undirected graphs.
    Visualization parameters can be customized as needed.

# Contact
    GitHub: github.com/cloner174
    Email: cloner174.org@gmail.com