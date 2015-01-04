from Class_SinglyLinkedList import *
from Class_SinglyLinkedQueue import *
from Class_SinglyLinkedStack import *
from collections import defaultdict

"""
        This is a collection of Forward and Reverse Breadth and Depth Searches written in Python. They are adapted 
        from the code I wrote for the course OR 643 Network Optimization, orginally in VBA. The algorthims come from
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
                CurrentArc[node] = AdjArray_arg.data[node].GetListHead
                PredArray_arg[SourceNode_arg] = SinglyLinkedQueueItem(None)

        MarkedArray_arg[SourceNode_arg] = True #Mark node s
        myNext = 1 #Next = 1
        OrderArray_arg[SourceNode_arg] = myNext #Order = 1      
        
        # Building the initial queue
        MyQueue = SinglyLinkedQueue()
        MyQueue.Add(SourceNode_arg) # List = s  
        PredArray_arg[SourceNode_arg] = SinglyLinkedQueueItem(None)

        # Main Loop
        while not MyQueue.IsEmpty(): # Do while List <> {}
                iNode = MyQueue.qFront # Select node i
                jNode = CurrentArc[iNode.Node]
                if not jNode is None:
                        if MarkedArray_arg[jNode.HeadNode] == False: # If node i is incident to an admissible arc (i,j) then
                                MarkedArray_arg[jNode.HeadNode] = True # Mark node j
                                PredArray_arg[jNode.HeadNode] = iNode # Predecessor(j) = i
                                myNext += 1 # next = next + 1
                                OrderArray_arg[jNode.HeadNode] = myNext # order(j) = next
                                MyQueue.Add(jNode.HeadNode)
                        CurrentArc[iNode.Node] = CurrentArc[iNode.Node].NextItem
                else:
                        MyQueue.Remove()
        return MarkedArray_arg, PredArray_arg, OrderArray_arg                

# Forward Depth Search Algorithm

"""

        This module accepts a source node and an adjacency array.  It performs a depth search meaning it takes each
        node it comes too moves to another node it is connected to and so on until the path ends.  It then returns to 
        the previous node and searches again until a path ends and so on and so on.  

"""

def FSearchD(SourceNode_arg, AdjArray_arg):

        MarkedArray_arg = defaultdict(bool)
        CurrentArc = defaultdict(SinglyLinkedListItem)
        PredArray_arg = defaultdict(SinglyLinkedStackItem)
        OrderArray_arg = defaultdict(int)

        # Initializing variables and data structures       
        for node in AdjArray_arg.data.keys():
                MarkedArray_arg[node] = False
                CurrentArc[node] = AdjArray_arg.data[node].GetListHead
                PredArray_arg[node] = SinglyLinkedStackItem(None)

        MarkedArray_arg[SourceNode_arg] = True #Mark node s
        myNext = 1 #Next = 1
        OrderArray_arg[SourceNode_arg] = myNext #Order = 1          

        # Building the initial stack
        MyStack = SinglyLinkedStack()
        MyStack.Push(SourceNode_arg) # List = S
        
        # Main Loop
        while not MyStack.StackEmpty(): # Do while List <> {}
                iNode = MyStack.sTop # Select node i
                jNode = CurrentArc[iNode.Node]
                if not jNode is None:
                        if not MarkedArray_arg[jNode.HeadNode]: # If node i is incident to an admissible arc (i,j) then
                                MarkedArray_arg[jNode.HeadNode] = True # Mark node j
                                PredArray_arg[jNode.HeadNode] = iNode # Predecesor(j) = 1
                                myNext += 1 # Next = Next + 1
                                OrderArray_arg[jNode.HeadNode] = myNext # Order(j) = next
                                MyStack.Push(jNode.HeadNode) # Add node j to List
                        CurrentArc[iNode.Node] = CurrentArc[iNode.Node].NextItem
                else:
                        MyStack.Pop()            
        print("i",i)   
        return MarkedArray_arg, PredArray_arg, OrderArray_arg 
        
