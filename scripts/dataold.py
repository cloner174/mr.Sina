#        #          #                    In the name of God   #    #
#
#GitHub.com/cloner174
#cloner174.org@gmail.com
#
import re

class DataHandle:
    def __init__(self,
                 data_links : dict, 
                 data_nodes : dict, 
                 layer_one_name:str = 'Advertisers', 
                 layer_two_name:str = 'Publishers'):
        self.data_nodes = data_nodes
        self.data_linkes = data_links
        self.layer_one_name = layer_one_name
        self.layer_two_name = layer_two_name
    
    def initial_keys(self, 
                     node_id_laybel : str = None, 
                     node_name_laybel : str = None,
                     node_color_laybel : str = None,
                     node_type_laybel : str = None,
                     logic_for_type_laybel : dict = None,
                     edges_source_laybel : str = None,
                     edges_target_laybel : str = None ,
                     graph_index_laybel_in_node_data : str = None,
                     graph_index_laybel_in_edge_data : str = None,
                     edges_id_laybel : str = None ):
        data_nodes_keys = list( self.data_nodes.keys() )
        data_links_keys = list( self.data_linkes.keys() )
        if node_id_laybel is not None :
            self.nodes_id_laybel = node_id_laybel
        else:
            for any_key in data_nodes_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_id = re.search( r'id', temp)
                if temp_initial_id is not None :
                    self.nodes_id_laybel = temp_key
                else:
                    continue
            if getattr(self, 'nodes_id_laybel', None) is not None :
                pass
            else:
                raise KeyError( " Can not find id for nodes ! Please pass the laybel to this method argumants .")
        if node_name_laybel is not None :
            self.nodes_name_laybel = node_name_laybel
        else:
            for any_key in data_nodes_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_name = re.search( r'name', temp)
                if temp_initial_name is not None :
                    self.nodes_name_laybel = temp_key
                else:
                    continue
        if node_color_laybel is not None :
            self.nodes_color_laybel = node_color_laybel
        else:
            for any_key in data_nodes_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_color_1 = re.search( r'color', temp)
                temp_initial_color_2 = re.search( r'colour', temp)
                temp_initial_color_3 = re.search( r'colors', temp)
                temp_initial_color_4 = re.search( r'colours', temp)
                if temp_initial_color_1 is not None or temp_initial_color_2 is not None or temp_initial_color_3 is not None or temp_initial_color_4 is not None:
                    self.nodes_color_laybel = temp_key
                else:
                    continue
        if node_type_laybel is not None :
            self.nodes_type_laybel = node_type_laybel
        else:
            for any_key in data_nodes_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_type = re.search( r'type', temp)
                if temp_initial_type is not None :
                    self.node_type_laybel = temp_key
                else:
                    continue
        if logic_for_type_laybel is not None :
            self.logic_for_types = logic_for_type_laybel
        if edges_source_laybel is not None :
            self.edge_source_laybel = edges_source_laybel
        else:
            for any_key in data_links_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_source = re.search( r'source', temp)
                if temp_initial_source is not None :
                    self.edge_source_laybel = temp_key
                else:
                    continue
            if getattr(self, 'edge_source_laybel', None) is not None :
                pass
            else:
                raise KeyError( " Can not find source column for edges ! Please pass the laybel to this method argumants .")
        if edges_target_laybel is not None :
            self.edge_target_laybel = edges_target_laybel
        else:
            for any_key in data_links_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()        
                temp_initial_target = re.search( r'target', temp)
                if temp_initial_target is not None :
                    self.edge_target_laybel = temp_key
                else:
                    continue
            if getattr(self, 'edge_target_laybel', None) is not None :
                pass
            else:
                raise KeyError( " Can not find target column for edges ! Please pass the laybel to this method argumants .")
        if graph_index_laybel_in_node_data is not None:
            self.graph_index_laybel_in_nodes_data = graph_index_laybel_in_node_data
        else:
            for any_key in data_links_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()
                temp_initial_index = re.search( r'index', temp )
                if temp_initial_index is not None :
                    self.graph_index_laybel_in_nodes_data = temp_key
                else:
                    continue
        if graph_index_laybel_in_edge_data is not None :
            self.graph_index_laybel_in_edges_data = graph_index_laybel_in_edge_data
        else:
            for any_key in data_links_keys :
                temp_key = str(any_key)
                temp = temp_key.lower()
                temp_initial_index = re.search( r'index', temp )
                if temp_initial_index is not None :
                    self.graph_index_laybel_in_edges_data = temp_key
                else:
                    continue
        if edges_id_laybel is not None :
            self.edge_id_laybel = edges_id_laybel
        self.advertiser_nodes = []
        self.publisher_nodes = []
        if getattr(self, 'nodes_name_laybel', None) is not None :
          try:  
            for i in range( len( self.data_nodes[self.nodes_name_laybel] )) :
                temp_name = self.data_nodes[self.nodes_name_laybel][i]
                temp_id = self.data_nodes[self.nodes_id_laybel][i]
                temp_advertiser = re.search( '^a', temp_name )
                temp_publisher = re.search( '^p', temp_name )
                if temp_advertiser is not None :
                    self.advertiser_nodes.append(temp_id)
                elif temp_publisher is not None :
                    self.publisher_nodes.append(temp_id)
                else:
                    continue
          except:
            raise KeyError( "\n there is no ID for nodes in data. Pass the id_laybel to node_id_laybel arguman of this Function !")
    
    def initial_data(self, 
                     need_nodes : bool = False,
                     edge_laybels : tuple = None , 
                     node_id_laybel : str = None,
                     advertiser_nodes : list = None ,
                     publisher_nodes : list = None ,
                     color_laybel : str = None ) :
        
        if edge_laybels is not None :
            self.edge_source_laybel = str( edge_laybels[0] )
            self.edge_target_laybel = str( edge_laybels[1] )
        else:
            try:
                if node_id_laybel is not None :
                    if color_laybel is not None:
                        self.initial_keys(node_id_laybel = node_id_laybel , color_laybel = color_laybel )
                    else:
                        self.initial_keys(node_id_laybel = node_id_laybel)
                else:
                    self.initial_keys()
                if getattr(self, 'edge_source_laybel', None) is not None and getattr(self, 'edge_target_laybel', None) is not None:
                    pass
                else:
                    raise KeyError( "\n there is no Laybel for source/target nodes ! pass the edge_laybels : touple arguman to this Function . ")
            except Exception as e :
                raise KeyError( f" there was something wrong with runnig seccseusesfully method initial_keys from this class -->> {e} <<-- try ruunig it manuualy and ")
        if advertiser_nodes is not None :
            self.advertiser_nodes = advertiser_nodes
        if publisher_nodes is not None:
            self.publisher_nodes = publisher_nodes
        if isinstance(self.advertiser_nodes, list) :
            if len(self.advertiser_nodes) == 0 :
                raise ValueError( " Please pass the advertiser_nodes to this Function Manually !")
            else:
                pass
        else:
            raise ValueError( " Please pass the advertiser_nodes to this Function Manually !!! IT MUST BE of TYPE List !!!")
        if isinstance(self.publisher_nodes, list) :
            if len(self.publisher_nodes) == 0 :
                raise ValueError( " Please pass the publisher_nodes to this Function Manually !")
            else:
                pass
        else:
            raise ValueError( " Please pass the publisher_nodes to this Function Manually !!! IT MUST BE of TYPE List !!!")            
        if need_nodes == True :
            return self.advertiser_nodes, self.publisher_nodes
    
    def modify_links(self, 
                     len_of_sources_and_targets : int = None ,
                     sources : list = None,
                     targets : list = None) :
        print( " Getting things Ready . . . ")
        temp_sources = list(self.data_linkes[self.edge_source_laybel])
        temp_targets = list(self.data_linkes[self.edge_target_laybel])
        if len_of_sources_and_targets is not None:
            len_of_rows = len_of_sources_and_targets
        else:
            len_of_sources = len( temp_sources )
            len_of_targets = len( temp_targets )
            if len_of_sources is not None and len_of_sources != 0 and len_of_sources == len_of_targets:
                len_of_rows = len_of_sources
            else:
                raise ValueError( " the len of sources and the targets are not Equal or its empty! Try passing the source and targets length to this function Or if its Not work. try passing source and target to this function!")
        if sources is not None:
            if not len_of_sources_and_targets:
                len_of_rows = int( input( " Please input the equal len of edge_source and edge_target here : It should be an int number and must be equal to targets length"))
            self.edge_source_laybel = 'source'
            temp_sources = sources
        if targets is not None:
            if not len_of_sources_and_targets:
                len_of_rows = int( input( " Please input the equal len of edge_source and edge_target here : It should be an int number and must be equal to sources length"))
            self.edge_target_laybel = 'target'
            temp_targets = targets            
        layer_one_links = []
        layer_two_links = []
        interconnected_links = []
        for j in range( len_of_rows ):
            edge = tuple( (temp_sources[j], temp_targets[j]) )
            source_temp = edge[0]
            target_temp = edge[1]
            if source_temp in self.advertiser_nodes:
                if target_temp in self.advertiser_nodes:
                    layer_one_links.append(edge)
                else:
                    if target_temp in self.publisher_nodes:
                        interconnected_links.append(edge)
            elif source_temp in self.publisher_nodes:
                if target_temp in self.publisher_nodes:
                    layer_two_links.append( edge )
                else:
                    if target_temp in self.advertiser_nodes:
                        interconnected_links.append(edge) 
        return layer_one_links, layer_two_links, interconnected_links

#end#