from Class_SinglyLinkedList import *
from Class_SinglyLinkedQueue import *
from collections import defaultdict

"""
        Topological Sort Algorthim:
        This routine takes an adjacency array, and returns whether a network is cyclic (True if it is cyclic)
        and returns the topological order of the network optionally.

"""

def Topological_Sort(MyAdjArray):

        MyQueue = SinglyLinkedQueue()
        NextCounter = 0

        # The In-Degree is a count of the number of Arcs/Edges wherein the respective node is the headnode.
        # Building the In-Degree list
        InDegree = defaultdict(int)
        for node in MyAdjArray.data.keys():
                MyListItem = MyAdjArray.data[node].GetListHead
                while not MyListItem is None:
                        InDegree[MyListItem.HeadNode] += 1
                        MyListItem = MyListItem.NextItem

        # Main Topological Sort Algorithm 
        # Test for 0 degree in In-Degree
        for node in MyAdjArray.data.keys():
                if InDegree[node] == 0:
                        MyQueue.Add(node)

        #Reduce the degree of the HeadNodes by 1  
        OrderList_arg = defaultdict(int)            
        while not MyQueue.IsEmpty():
                MyQueueItem = MyQueue.Remove()
                NextCounter += 1
                OrderList_arg[MyQueueItem.Node] = NextCounter
        
                MyListItem = MyAdjArray.data[MyQueueItem.Node].GetListHead
                while not MyListItem is None:
                        InDegree[MyListItem.HeadNode] -= 1
                        if InDegree[MyListItem.HeadNode] == 0:
                                MyQueue.Add(MyListItem.HeadNode)
                        MyListItem = MyListItem.NextItem
        
        #Returned Results
        if NextCounter < MyAdjArray.Count:
                IsCyclic_arg = True
 
        return IsCyclic_arg, OrderList_arg
                
