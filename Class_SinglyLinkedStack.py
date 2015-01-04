# Singly Linked Stack Item
"""     
        This is a class for a Singly Linked Stack Item data structure.  
        It is initialized by OPTIONALLY passing a Node name, an Optional Label, 
        and an optional Next List Item.  It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz 
        and Mike Gilbert, Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted by me from the VBA code for that course. 

        Attributes:
                .Node - Singly Linked Stack Item 
                .Label - Optional Data variable; Various Uses but mainly for labeling Stack items for Network Modeling
                .NextItem - Pointer to the Next Singly Linked Stack Item 

        Methods:
                .SetNextItem - Method to set a Stack Item's .NextItem attribute
                .SetLabel - Method to set a Stack Items's .Label attribute
"""   
class SinglyLinkedStackItem(object):

        def __init__(self, slsi_Node, slsi_Label = None, slsi_NextItem = None):
                self.Node = slsi_Node
                self.Label = slsi_Label 
                self.NextItem = slsi_NextItem             
        
        def SetNextItem(self, slsi_tempHdNode):
                self.NextItem = slsi_tempHdNode

        def SetLabel(self, slsi_tempLabel):
                self.Label = slsi_tempLabel

        def __Terminate__(self):
                self.NextItem = None 

# SinglyLinkedStack Class 
"""      
        This Stack class is adapted from VBA code from the course OR 643 Network Optimization. 
        It is a minor modification From 'the "VBA Developer's Handbook, 2nd Edition"
        by Ken Getz and Mike Gilbert  Copyright 2001; Sybex, Inc. All rights reserved. The VBA code 
        was given to me by Professor Steven Charbonneau. It is adapted by me from the VBA code for that course. 

        Attributes:
                .sTop - Pointer to the Stack Item at the top of the Stack 
                .sCount - Counter that tracks the number of Stack Items in the Stack

        Methods:
                .IsEmpty - Returns boolean True if the Stack is empty and false if it contains a Stack Item
                .Pop - Deletes the Stack Item at the top of the Stack and returns it
                .Push - Adds a Stack Item to the top of the  Stack
                        Use:
                                SinglyLinkedStackObject.Add(Node_Label, Optional Data_Label) 
                                Where:
                                        Node_Label - Node Label
                                        Data_Label - Optional Data Label; Mainly used for labeling nodes in Network
                                                     Optimization Algorithms          
"""

class SinglyLinkedStack(object):

        def __init__(self):
                
                self.sTop = None
                self.sCount = 0

        def Pop(self):
                
                if self.StackEmpty():
                        return None
                else:
                        self.sCount -= 1
                        TempTop = self.sTop
                        self.sTop = TempTop.NextItem
                        return TempTop

        def Push(self, _EndNode, _Label = None):

                _NewStackItem = SinglyLinkedStackItem(_EndNode, _Label, self.sTop)
                self.sTop = _NewStackItem
                self.sCount += 1
                
        def StackEmpty(self):

                if self.sTop is None:
                        return True
                else:
                        return False
        
        def __Terminate__(self):
                
                self.sTop = None
        
        
