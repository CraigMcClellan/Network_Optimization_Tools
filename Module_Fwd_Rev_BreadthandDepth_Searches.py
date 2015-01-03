from Class_SinglyLinkedList import *
from Class_SinglyLinkedQueue import *
from collections import defaultdict

"""
        This is a collection of Forward and Reverse Breadth and Depth Searches written in Python. They are adapted 
        from VBA code I wrote for the course Or 643 Netowrk Optimization, orginally in VBA. The algorthims come from
        the text:

        Algorithm From Network Flows: Ravindra K. Ahuja; Thomas L. Magnanti; James B. Orlin
        ISBN: 978-0-13-617549-0     

        These implemenations use Singly Linked Lists and Queues(?) and Adjacency Array Classes imported from the 
        above files.  All should be found my Github Network Optimization Tools Repository. 

        contact: craig.j.mcclellan@gmail.com

"""
# Forward Breadth Search Algorithm
"""

        This module accepts a source node and an adjacency array.  It performs a breadth search meaning it takes each
        node it comes too and searches each arc connected to that node before it moves on to another node.

"""

def FSearchB(SourceNode_arg, AdjArray_arg):

        MarkedArray_arg = defaultdict(bool)
        CurrentArc = defaultdict(SinglyLinkedListItem)
        PredArray_arg = defaultdict(SinglyLinkedQueueItem)
        OrderArray_arg = defaultdict(int)

        # Initializing variables and data structures       
         for node in AdjArray_arg.data.keys():
                MarkedArray_arg[node] = False
                CurrentArc[node] = AdjArray.data[node].GetListHead

        MarkedArray_arg[SourceNode_arg] = True #Mark node s
        myNext = 1 #Next = 1
        OrderArray_arg[SourceNode_arg] = myNext #Order = 1
        # Not instantiating PredArray_arg[SourceNode_arg] will make it None(?)
        PredArray_arg[SourceNode_arg]
        
        # Building the initial queue
        MyQueue = SinglyLinkedQueue()
        MyQueue.Add(SourceNode_arg) # List = s  

        # Main Loop
        while not MyQueue.IsEmpty(): # Do while List <> {}
                iNode = MyQueue.qFront # Select node i
                jNode = CurrentArc[iNode.Node]
                if not jNode is None:
                        if MarkedArray_arg[jNode.HeadNode] = False: # If node i is incident to an admissible arc (i,j) then
                                MarkedArray_arg[jNode.HeadNode] = True # Mark node j
                                PredArray_arg[jNode.HeadNode] = iNode # Predecessor(j) = i
                                myNext += 1 # next = next + 1
                                OrderArray_arg[jNode.HeadNode] = myNext # order(j) = next
                                MyQueue.Add(jNode.HeadNode)
                        CurrentArc[iNode.Node] = CurrentArc[iNode.Node].NextItem
                else:
                        MyQueue.Remove

        return MarkedArray_arg, PredArray_arg, OrderArray_arg                
