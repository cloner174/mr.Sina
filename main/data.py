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
    
    def initial_keys(self, node_id_laybel : str = None, color_laybel : str = None):
        data_nodes_keys = list( self.data_nodes.keys() )
        data_links_keys = list( self.data_linkes.keys() )
        for any_key in data_nodes_keys :
            temp_key = str(any_key)
            temp = temp_key.lower()
            temp_initial_id = re.search( r'id', temp)
            temp_initial_name = re.search( r'name', temp)
            temp_initial_index = re.search( r'index', temp )
            temp_initial_type = re.search( r'type', temp )
            temp_initial_color_1 = re.search( r'color', temp)
            temp_initial_color_2 = re.search( r'colour', temp)
            temp_initial_color_3 = re.search( r'colors', temp)
            temp_initial_color_4 = re.search( r'colours', temp)
            if temp_initial_color_1 is not None or temp_initial_color_2 is not None or temp_initial_color_3 is not None or temp_initial_color_4 is not None:
                self.nodes_color_laybel = temp_key
            if temp_initial_id is not None :
                self.nodes_id_laybel = temp_key
            if temp_initial_name is not None :
                self.nodes_name_laybel = temp_key
            if temp_initial_index is not None :
                self.graph_index_laybel = temp_key
            if temp_initial_type is not None :
                self.nodes_type_laybel = temp_key
        for any_key in data_links_keys :
            temp_key = str(any_key)
            temp = temp_key.lower()
            temp_initial_source = re.search( r'source', temp)
            temp_initial_target = re.search( r'target', temp)
            temp_initial_index = re.search( r'index', temp )
            temp_initial_id = re.search( r'id', temp )
            if temp_initial_source is not None :
                self.edge_source_laybel = temp_key
            if temp_initial_target is not None :
                self.edge_target_laybel = temp_key
            if temp_initial_id is not None :
                self.edge_id_laybel = temp_key
            if temp_initial_index is not None :
                self.graph_index_laybel = temp_key
        if node_id_laybel is not None:
            self.nodes_id_laybel = node_id_laybel
        if color_laybel is not None :
            self.nodes_color_laybel = color_laybel
        self.adertiser_nodes = []
        self.publisher_nodes = []
        if getattr(self, 'nodes_name_laybel', None) is not None :
          try:  
            for i in range( len( self.data_nodes[self.nodes_name_laybel] )) :
                temp_name = self.data_nodes[self.nodes_name_laybel][i]
                temp_id = self.data_nodes[self.nodes_id_laybel][i]
                temp_advertiser = re.search( '^a', temp_name )
                temp_publisher = re.search( '^p', temp_name )
                if temp_advertiser is not None :
                    self.adertiser_nodes.append(temp_id)
                elif temp_publisher is not None :
                    self.publisher_nodes.append(temp_id)
                else:
                    continue
          except:
            raise KeyError( "\n there is no ID for nodes in data. Pass the id_laybel to node_id_laybel arguman of this Function !")
    
    def initial_data(self, 
                     edge_laybels : tuple = None , 
                     node_id_laybel : str = None,
                     adertiser_nodes : list = None ,
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
        if adertiser_nodes is not None :
            self.adertiser_nodes = adertiser_nodes
        if publisher_nodes is not None:
            self.publisher_nodes = publisher_nodes
        if isinstance(self.adertiser_nodes, list) :
            if len(self.adertiser_nodes) == 0 :
                raise ValueError( " Please pass the adertiser_nodes to this Function Manually !")
            else:
                pass
        else:
            raise ValueError( " Please pass the adertiser_nodes to this Function Manually !!! IT MUST BE of TYPE List !!!")
        if isinstance(self.publisher_nodes, list) :
            if len(self.publisher_nodes) == 0 :
                raise ValueError( " Please pass the publisher_nodes to this Function Manually !")
            else:
                pass
        else:
            raise ValueError( " Please pass the publisher_nodes to this Function Manually !!! IT MUST BE of TYPE List !!!")            
    
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
            if source_temp in self.adertiser_nodes:
                if target_temp in self.adertiser_nodes:
                    layer_one_links.append(edge)
                else:
                    if target_temp in self.publisher_nodes:
                        interconnected_links.append(edge)
            elif source_temp in self.publisher_nodes:
                if target_temp in self.publisher_nodes:
                    layer_two_links.append( edge )
                else:
                    if target_temp in self.adertiser_nodes:
                        interconnected_links.append(edge) 
        return layer_one_links, layer_two_links, interconnected_links

#end#