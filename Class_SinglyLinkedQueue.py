# SinglyLinkedQueueItem Class
"""     This is a class for a Singly Linked Queue Item data structure.  
        It is initialized by OPTIONALLY passing a Node name, an Optional Label, 
        and an optional Next List Item.  It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz 
        and Mike Gilbert, Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted by me from the VBA code for that course. 

        Attributes:
                .Node - Singly Linked Queue Item 
                .Label - Optional Data variable; Various Uses but mainly for labeling queue items for Network Modeling
                .NextItem - Pointer to the Next Singly Linked Queue Item 

        Methods:
                .SetNextItem - Method to set a Queue Item's .NextItem attribute
                .SetLabel - Method to set a Queue Items's .Label attribute
"""

class SinglyLinkedQueueItem(object):

        def __init__(self, slqi_Node, slqi_Label = None, slqi_NextItem = None):
                self.Node = slqi_Node
                self.Label = slqi_Label 
                self.NextItem = slqi_NextItem             
        
        def SetNextItem(self, slqi_tempHdNode):
                self.NextItem = slqi_tempHdNode

        def SetLabel(self, slqi_tempLabel):
                self.Label = slqi_tempLabel

        def __Terminate__(self):
                self.NextItem = None 

# SinglyLinkedQueue Class
"""      
        This queue class is adapted from VBA code from the course OR 643 Network Optimization. 
        It is a minor modification From 'the "VBA Developer's Handbook, 2nd Edition"
        by Ken Getz and Mike Gilbert  Copyright 2001; Sybex, Inc. All rights reserved. The VBA code 
        was given to me by Professor Steven Charbonneau. It is adapted by me from the VBA code for that course. 

        Attributes:
                .qFront - Pointer to the Queue Item at the front of the queue 
                .qRear - Pointer to the Queue Item at the rear of the queue
                .qCount - Counter that tracks the number of Queue Items in the Queue

        Methods:
                .IsEmpty - Returns boolean True if the Queue is empty and false if it contains a Queue Item
                .Remove - Deletes the Queue Item at the front of the Queue and returns it
                .Add - Adds a Queue Item to a Queue
                        Use:
                                SinglyLinkedQueueObject.Add(Node_Label, Optional Data_Label) 
                                Where:
                                        Node_Label - Integer Node abel
                                        Data_Label - Optional Data Label; Mainly used for labeling nodes in Network
                                                     Optimization Algorithms
          
"""
class SinglyLinkedQueue(object):

        def __init__(self):
                self.qFront = None # Pointer to the front of the queue where items are removed
                self.qRear = None  # Pointer to the rear of the queue where items are added
                self.qCount = 0 # C

        def IsEmpty(self):
        
                if self.qFront is None and self.qRear is None:
                        return True
                else:
                        return False
        
        def Remove(self):
                if self.IsEmpty(): # If the queue is empty return None
                        print("Error - Trying to .Remove from an empty Queue!")
                        __TempPointer =  None
                else: 
                        __TempPointer = self.qFront
                        if self.qFront is self.qRear: # If there is only one item
                                self.qFront = None
                                self.qRear = None
                        else: # If more than one item
                                self.qFront = self.qFront.NextItem
                        self.qCount -= 1
                return __TempPointer    

        def Add(self, _EndNode, Data_Label = None):
        
                qNew = SinglyLinkedQueueItem( _EndNode, Data_Label) # Create new Queue Item

                if self.IsEmpty(): 
                        self.qFront = qNew
                        self.qRear = qNew
                else:
                        self.qRear.SetNextItem(qNew)
                        self.qRear = qNew

                self.qCount += 1

        def qPrint(self):

                print("Singly Linked Queue :", end = " ")
                slqi_MyQueueItem = self.qFront
                while not slqi_MyQueueItem is None:
                        print(slqi_MyQueueItem.Node, end = " ")
                        slqi_MyQueueItem = slqi_MyQueueItem.NextItem
                print("\n")

        def __Terminate__(self):
                self.qFront = None
                self.qRear = None
