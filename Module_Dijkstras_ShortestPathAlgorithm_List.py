from collections import defaultdict
import csv # Comma Seperated Variable Module
from Class_SinglyLinkedList import *

# Dijkstra's Shortest Path Algorithm using lists
"""    
        Implementation of Dijkstra's Shortest Path Algorithm to find the shortest path
        from a Source Node to all other nodes in a network.  This is the most least efficient
        implementation using only Singly Linked Lists. 

        This implementation is done using Singly Linked Lists and My own Adjacency Array Class. 
"""

def SPA_Dijkstra(SourceNode_arg, AdjArray_arg):

        # Initializations 
        InfDist = 32000         #This is a VLN (Very Large Number) distance used to set the initial distances of each node; 
                                #It is 32k because of the size limitation of integers 
        
        SouceNode_arg = SourceNode_arg # insurance        

        DistArray_arg = defaultdict(int) 
        PredArray_arg = defaultdict(int)       

        for nodes in AdjArray_arg.data.keys():
                DistArray_arg[nodes] = InfDist  # Distance(i) = VLN for all i in N
                PredArray_arg[nodes] = -1       # Pred(i) = -1 for all i in N         
                
        S = SinglyLinkedList()   # S = {} 
        S_Prime = SinglyLinkedList() #Both S and S' are SinglyLinkedLists where AdjArray.data is an "array" of lists                                                     
        for nodes in AdjArray_arg.data.keys():  # S' = N              
                S_Prime.AddItem(nodes) # We are putting all the nodes in S_Prime but these nodes are NOT SinglyLinkedListItems just keys

        #S_Prime = [int(i) for i in S_Prime]
        
        DistArray_arg[SourceNode_arg] = 0       # Distance(Source) = 0
        PredArray_arg[SourceNode_arg] = 0       # Predecessor(Source) = 0
 
        while S.Count < AdjArray_arg.Count:       # Main Loop
                
                # Find the smallest Distance in S' and point to it with MinListItems                  
                MyListItem = S_Prime.GetListHead         
                MinListItem = MyListItem 
                while not MyListItem is None:
                        if DistArray_arg[MyListItem.HeadNode] < DistArray_arg[MinListItem.HeadNode]:
                                MinListItem = MyListItem
                        MyListItem = MyListItem.NextItem

                # Add the shortest distance node to the S List and Remove it from S' thus marking it permanent
                S.AddItem(MinListItem.HeadNode)
                S_Prime.Delete(MinListItem.HeadNode)

                # For (i,j) in A(i,j)
                MyListItem = AdjArray_arg.data[MinListItem.HeadNode].GetListHead
                while not MyListItem is None:
                        if DistArray_arg[MyListItem.HeadNode] > DistArray_arg[MinListItem.HeadNode] + MyListItem.ArcCost: #if D(j) > D(i) + c(i,j)
                                DistArray_arg[MyListItem.HeadNode] = DistArray_arg[MinListItem.HeadNode] + MyListItem.ArcCost #then D(j) = D(i) + c(i,j)  
                                PredArray_arg[MyListItem.HeadNode] = MinListItem.HeadNode # Predecessor(j) = i
                        MyListItem = MyListItem.NextItem                                   
                
        return DistArray_arg, PredArray_arg 
