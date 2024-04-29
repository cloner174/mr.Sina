#        #          #                    In the name of God   #    #
#
#GitHub.com/cloner174
#cloner174.org@gmail.com
#
from time import sleep
import networkx as nx

class Graph :
    def __init__( self, layer_one_name : str, layer_two_name : str , nx_use : bool = False ) :
        self.layer_one_name = layer_one_name
        self.layer_two_name = layer_two_name
        self.nx_use = nx_use
        if nx_use:
            pass
        else:
            from pymnet import MultilayerNetwork, draw
    
    def create( self, Aspects = 1, fully_Interconnect = False ) :
        print( " Starting to Create Graph . . . ")
        sleep(1)
        print( " The default values for aspects, fullyInterconnected and nx_use arguments are 1 and False. " )
        sleep(1)
        if self.nx_use:
            print( "You choosed a Network of type NetWorkX Graph Creation !")
            sleep(1)
            G = nx.Graph()
            print( "Successfully Create The Graph Object !")
            sleep(1)
            return G
        g = MultilayerNetwork( aspects = Aspects, fullyInterconnected = fully_Interconnect )
        print( "Successfully Create The Graph Object !")
        sleep(1)
        print( " Adding layers . . . ")
        sleep(1)
        g.add_layer( self.layer_one_name )
        g.add_layer( self.layer_two_name )        
        print(" Done !")
        sleep(1)
        print( g.get_layers() )
        sleep(1)
        return g
    
    def add_node(self,
                 nodes_to_add : list,
                 nx_use = True ,
                 G = None):
        if self.nx_use == False:
            print(" Not Implantted Yet ! no need actully ! use add_links method instead !")
            return
        else:
            pass
        if G is not None :
            pass
        else:
            G = nx.Graph()
        G.add_nodes_from(nodes_to_add)
        return G
    
    def add_links(self,
                  layer_one_links : list,
                  layer_two_links : list,
                  Interconnected_links : list,
                  layer_one_nodes : list = None,
                  layer_two_nodes : list = None,
                  just_interconnect_for_nx_graph : bool = False,
                  G = None):
        if G is not None :
            g = G
        else:
            if self.nx_use :
                if layer_one_nodes is not None :
                    if layer_two_nodes is not None :
                        interconnected_nodes = layer_one_nodes.copy()
                        for i in layer_two_nodes :
                            if i not in interconnected_nodes:
                                interconnected_nodes.append(i)
                        interconnected_g = nx.Graph()
                        interconnected_g = self.add_node( G = interconnected_g , nodes_to_add = interconnected_nodes )
                        if just_interconnect_for_nx_graph == True :
                            pass
                        else:
                            layer_one_g = nx.Graph()
                            layer_two_g = nx.Graph()
                            layer_one_g = self.add_node( G = layer_one_g , nodes_to_add = layer_one_nodes )
                            layer_two_g = self.add_node( G = layer_two_g , nodes_to_add = layer_two_nodes )
                    else:
                        pass
                else:
                    import pandas as pd
                    layer_one_node_temp = []
                    for i in layer_one_links:
                        if i[0] not in  layer_one_node_temp :
                            layer_one_node_temp.append(i[0])
                            continue
                        if i[1] not in layer_one_node_temp :
                            layer_one_node_temp.append(i[1])
                            continue
                    layer_two_node_temp = []                
                    for i in layer_two_links:
                        if i[0] not in layer_two_node_temp :
                            layer_two_node_temp.append(i[0])
                            continue
                        if i[1] not in layer_two_node_temp :
                            layer_two_node_temp.append(i[1])
                            continue
                    for i in Interconnected_links :
                        if i[0] not in layer_one_node_temp :
                            layer_one_node_temp.append(i[0])
                            continue
                        if i[1] not in layer_one_node_temp :
                            layer_one_node_temp.append(i[1])
                            continue
                        if i[0] not in layer_two_node_temp :
                            layer_two_node_temp.append(i[0])
                            continue
                        if i[1] not in layer_two_node_temp :
                            layer_two_node_temp.append(i[1])
                            continue
                        interconnected_nodes = layer_one_node_temp.copy()
                        for i in layer_two_node_temp :
                            if i not in interconnected_nodes:
                                interconnected_nodes.append(i)
                    interconnected_g = nx.Graph()
                    interconnected_g = self.add_node( G = interconnected_g , nodes_to_add = interconnected_nodes )
                    if just_interconnect_for_nx_graph == True :
                        pass
                    else:
                        layer_one_node = pd.Series(layer_one_node_temp).unique()
                        layer_two_node = pd.Series(layer_two_node_temp).unique()
                        layer_one_g = nx.Graph()
                        layer_two_g = nx.Graph()
                        layer_one_g = self.add_node( G = layer_one_g , nodes_to_add = layer_one_node )
                        layer_two_g = self.add_node( G = layer_two_g , nodes_to_add = layer_two_node ) 
            else:
                g = self.create()
        for edge in layer_one_links:
            edgeSource = edge[0]
            edgeTarget = edge[1]
            if self.nx_use == True :
                interconnected_g.add_edge(edgeSource, edgeTarget)
                if just_interconnect_for_nx_graph == True :
                    pass
                else:
                    layer_one_g.add_edge(edgeSource, edgeTarget)
            else:
                g[ edgeSource, edgeTarget, self.layer_one_name , self.layer_one_name ] = 1
        for edge in layer_two_links:
            edgeSource = edge[0]
            edgeTarget = edge[1]
            if self.nx_use == True :
                interconnected_g.add_edge(edgeSource, edgeTarget)
                if just_interconnect_for_nx_graph == True :
                    pass
                else:
                    layer_two_g.add_edge(edgeSource, edgeTarget)
            else:
                g[ edgeSource, edgeTarget, self.layer_two_name, self.layer_two_name ] = 1
        for edge in Interconnected_links:
            edgeSource = edge[0]
            edgeTarget = edge[1]
            if self.nx_use == True :
                interconnected_g.add_edge(edgeSource, edgeTarget)
            else:
                g[edgeSource, edgeTarget, self.layer_one_name, self.layer_two_name ] = 1        
        if self.nx_use == True :
            if just_interconnect_for_nx_graph == True :
                return interconnected_g
            else:
                return layer_one_g, layer_two_g, interconnected_g
        else:
            return g
    
    def show(self, G, return_Graph_object = False ):
        if self.nx_use:
            print( "Not Implanted yet! use networkx docs " )
            return False
        print(" starting to show !")
        sleep(1)
        print(" this may take a few while ")
        sleep(1)
        print( " the defult value for return_Graph_object is False ")
        draw(G, layout = 'fr',layergap=2.5, layershape= 'circle',
                 nodeLabelRule = {} , show = True , alignedNodes = False, layerPadding = 0.1 )
        if return_Graph_object == True :
            return G

#end#
