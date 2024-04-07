#        #          #                    In the name of God   #    #
#
#GitHub.com/cloner174
#cloner174.org@gmail.com
#
import re

class DataHandle:
    def __init__(self, 
                 data_links: dict, 
                 data_nodes: dict, 
                 layer_one_name: str = 'Advertisers', 
                 layer_two_name: str = 'Publishers'):
        
        self.data_nodes = data_nodes
        self.data_links = data_links
        self.layer_one_name = layer_one_name
        self.layer_two_name = layer_two_name
    
    def initial_keys(self, 
                     node_id_label: str = None, 
                     node_name_label: str = None, 
                     node_color_label: str = None, 
                     node_type_label: str = None, 
                     logic_for_type_label: dict = None, 
                     edges_source_label: str = None, 
                     edges_target_label: str = None, 
                     graph_index_label_in_node_data: str = None, 
                     graph_index_label_in_edge_data: str = None, 
                     edges_id_label: str = None):
        
        data_nodes_keys = list(self.data_nodes.keys())
        data_links_keys = list(self.data_links.keys())
        
        def find_key(keys, pattern, default=None):
            for key in keys:
                if re.search(pattern, key, re.IGNORECASE):
                    return key
            return default
        
        self.nodes_id_label = node_id_label or find_key(data_nodes_keys, r'id', "id")
        if getattr(self, 'nodes_id_label', None) is not None :
            pass
        else:
            raise KeyError( " Can not find id for nodes ! Please pass the label to this method arguments .")
        self.nodes_name_label = node_name_label or find_key(data_nodes_keys, r'name', None)
        self.nodes_color_label = node_color_label or find_key(data_nodes_keys, r'color|colour', None)
        self.nodes_type_label = node_type_label or find_key(data_nodes_keys, r'type', None)
        self.logic_for_types = logic_for_type_label
        self.edge_source_label = edges_source_label or find_key(data_links_keys, r'source', "source")
        if getattr(self, 'edge_source_label', None) is not None :
            pass
        else:
            raise KeyError( " Can not find source column for edges ! Please pass the label to this method arguments .")
        self.edge_target_label = edges_target_label or find_key(data_links_keys, r'target', "target")
        if getattr(self, 'edge_target_label', None) is not None :
            pass
        else:
            raise KeyError( " Can not find target column for edges ! Please pass the label to this method arguments .")
        self.graph_index_label_in_nodes_data = graph_index_label_in_node_data or find_key(data_nodes_keys, r'index', None)
        self.graph_index_label_in_edges_data = graph_index_label_in_edge_data or find_key(data_links_keys, r'index', None)
        self.edge_id_label = edges_id_label or find_key(data_links_keys, r'id', None)
        
        self.advertiser_nodes = []
        self.publisher_nodes = []
        if getattr(self, 'nodes_name_label', None) is not None :
            print(self.nodes_name_label)
            for i in range(len(self.data_nodes[self.nodes_name_label])):
                temp_name = self.data_nodes[self.nodes_name_label][i]
                temp_id = self.data_nodes[self.nodes_id_label][i]
                if temp_name.startswith('a'):
                    self.advertiser_nodes.append(temp_id)
                elif temp_name.startswith('p'):
                    self.publisher_nodes.append(temp_id)
        else:
            print(" Unable to find any references or logic to split the nodes into layers " )
    
    def initial_data(self,
                     need_nodes: bool = False,
                     advertiser_nodes: list = None, 
                     publisher_nodes: list = None, 
                     color_label: str = None):
        if advertiser_nodes is not None and publisher_nodes is not None :
            self.advertiser_nodes = advertiser_nodes
            self.publisher_nodes = publisher_nodes
            return
        else:
            pass
        try:
            self.initial_keys()
            if need_nodes:
                return self.advertiser_nodes, self.publisher_nodes
        except:
            raise ValueError( " Please pass the advertiser_nodes and/or publisher_nodes to this Function Manually !!! \n IT MUST BE of TYPE List !!!")

    def modify_links(self, 
                     len_of_sources_and_targets=None, 
                     sources=None, 
                     targets=None):
        print("Getting things Ready...")
        if sources is not None and targets is not None:
            temp_sources = sources
            temp_targets = targets
        else:
            temp_sources = list(self.data_links[self.edge_source_label])
            temp_targets = list(self.data_links[self.edge_target_label])
    
        if len_of_sources_and_targets is not None:
            len_of_rows = len_of_sources_and_targets
        else:
            if len(temp_sources) != len(temp_targets):
                raise ValueError("The lengths of sources and targets are not equal or are empty! Please ensure they are correctly provided.")
            len_of_rows = len(temp_sources)
        
        advertiser_nodes_set = set(self.advertiser_nodes)
        publisher_nodes_set = set(self.publisher_nodes)
        
        layer_one_links = []
        layer_two_links = []
        interconnected_links = []
        
        for j in range(len_of_rows):
            source, target = temp_sources[j], temp_targets[j]
            if source in advertiser_nodes_set:
                if target in advertiser_nodes_set:
                    layer_one_links.append((source, target))
                elif target in publisher_nodes_set:
                    interconnected_links.append((source, target))
            elif source in publisher_nodes_set:
                if target in publisher_nodes_set:
                    layer_two_links.append((source, target))
                elif target in advertiser_nodes_set:
                    interconnected_links.append((source, target))
        
        return layer_one_links, layer_two_links, interconnected_links

#end#
