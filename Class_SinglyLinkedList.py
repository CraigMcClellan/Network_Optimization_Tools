# SinglyLinkedListItem Class 
"""     This is a class for a Singly Linked List Item  data structure.  
        It is initialized by OPTIONALLY passing the Head Node, Edge/Arc Cost, the UpperCapacity of the Edge/Arc,
        and the Next List Item.  It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz 
        and Mike Gilbert, Sybex, 2001. The VBA code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted from the VBA code for that course. 

        Also used these websites to understand SLLIs in Python :
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
        http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
        http://www.dreamincode.net/forums/topic/211480-python-singly-linked-lists/

        Attributes:        
        .HeadNode = Head Node, the node or list item flow pushed across this arc is directed to; default = None
        .ArcCost = Edge/Arc Cost, this is the cost or impact of pushing flow across this edge/arc; default = None 
        .UpperCapacity = The maximum amount of flow that can be pushed across this edge/arc; default = None
        .NextItem = The List Item or Node that follows this particular node as a SinglyLnkedListItem; default  = None       
        
        Methods:
        .SetNextItem - This method allows for the update of the NextItem attribute       

        
"""      
class SinglyLinkedListItem(object):

        def __init__(self, slli_HeadNode = None, slli_ArcCost = None, slli_UpperCapacity = None,  slli_NextItem = None):
                self.HeadNode = slli_HeadNode
                self.ArcCost = slli_ArcCost
                self.UpperCapacity = slli_UpperCapacity
                self.NextItem = slli_NextItem   # as SinglyLinkedListItem           
        
        def SetNextItem(self, slli_tempHdNode):
                self.NextItem = slli_tempHdNode # as SinglyLinkedListItem

        def __Terminate__(self):
                self.NextItem = None 

# SinglyLinkedList Class 
"""     This is a class for a Singly Linked List data structure. It is initialized with no parameters.
        It is modified code from "VBA Developer's Handbook, 2nd Edition" by Ken Getz and Mike Gilbert, 
        Sybex, 2001. This code was given to me by Professor Steven Charbonneau for the course OR 643
        Network Optimization.  It is adapted from the VBA code for that course. 

        Also used these websites to understand SLLs in Python :
        https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
        http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
        http://www.dreamincode.net/forums/topic/211480-python-singly-linked-lists/

        Attributes:
        .GetListHead - This returns the Singly Linked List Item that is in front of the list
        .Count - The number of Singly Linked List Items in the list

        Methods:
        .IsEmpty - Returns True if no Singly Linked List Items are in the List; False if a Singly Linked List 
                   Item exists in the List
        .AddItem - This method is used to add/create a Singly Linked List Item to/in the the List.  
                   Use:
                        SinglyLinkedListObject.AddItem(EndNode, EdgeCost (Optional), UpperCapacity (Optional), SortTerm (Optional), SortOrder (Optional))
                        Where:
                                EndNode - Head Node, the node or list item flow pushed across this arc is directed to
                                EdgeCost - Edge/Arc Cost, this is the cost or impact of pushing flow across this edge/arc; default = 0 
                                UpperCapacity - The maximum amount of flow that can be pushed across this edge/arc; default = None
                                SortTerm - An indicator of which term we are sorting on
                                                0 = No Sort (not currently used)
                                                1 = Sort on EndNode (Default value)
                                                2 = Sort on EdgeCost
                                SortOrder - An indicator of which way we want to sort the data
                                                "Asc" = Ascending Order (Default Value)
                                                "Desc" = Descending Order
        .Delete - This Method is used to delete a Singly Linked List Item from the List. Returns error if Item is not in the List.
                Use:
                SinglyLinkedListObject.Delete(EndNode)
                Where:
                        EndNode - Head Node, the node or list item flow pushed across this arc is directed to
        .sPrint - Prints out the Singly Linked List

        Updates:
        12/28/2014 - Completed and tested, planning on adding Lower Capacity Functionality at a later date
"""
class SinglyLinkedList(object): 
      
        def __init__(self):       
                
                self.GetListHead = None
                self.Count = 0         

        def IsEmpty(self):     
                if self.GetListHead is None: #.HeadNode is None:
                        return True   
                else:
                        return False  

        def AddItem(self, _EndNode, _EdgeCost = 0, _UpperCapacity = None, _SortTerm = 1, _SortOrder = 'Asc'):                              
                
                _liNew = SinglyLinkedListItem( _EndNode, _EdgeCost, _UpperCapacity)

                _liPrevious = None

                if self.GetListHead == None:                        
                        self.GetListHead = _liNew
                else:
                        _liCurrent = self.GetListHead 
                        if _SortTerm == 0:                        
                                while not _liCurrent is None:
                                        _liPrevious = _liCurrent
                                        _liCurrent = _liCurrent.NextItem                         
                        elif _SortTerm == 1: 
                                if _SortOrder == "Asc":
                                        while not _liCurrent is None:
                                                if _liNew.HeadNode > _liCurrent.HeadNode:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                                else:
                                        while not _liCurrent is None:
                                                if _liNew.HeadNode < _liCurrent.HeadNode:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break  
                        elif _SortTerm == 2:
                                if _SortOrder == "Asc":
                                        while not _liCurrent is None:
                                                if _liNew.ArcCost > _liCurrent.ArcCost:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                                else:
                                        while not _liCurrent is None:
                                                if _liNew.ArcCost < _liCurrent.ArcCost:
                                                        _liPrevious = _liCurrent
                                                        _liCurrent = _liCurrent.NextItem
                                                else:
                                                        break 
                        if _liPrevious == None:
                                _liNew.SetNextItem(self.GetListHead)
                                self.GetListHead = _liNew
                        else:                        
                                _liNew.SetNextItem(_liCurrent)
                                _liPrevious.SetNextItem(_liNew)

                self.Count += 1    
        
        def Delete(self, _TargetedNode):            

                #initialize the variables we will be using
                _liPrevious = None
                _liCurrent = self.GetListHead

                #iterate through the list until we reach the end
                while not _liCurrent is None:
                        if _liCurrent.HeadNode == _TargetedNode:
                                if _liPrevious is None:
                                        self.GetListHead = _liCurrent.NextItem
                                else:
                                        _liPrevious.NextItem = _liCurrent.NextItem
                                self.Count -= 1     
                                if self.Count == 0:
                                        self.GetListHead = None                              
                                _liCurrent = None
                        else:
                                _liPrevious = _liCurrent
                                _liCurrent = _liCurrent.NextItem  

        def sPrint(self):
        
                MyListItem = self.GetListHead
                print("Singly Linked List: ", end = " ")
                while not MyListItem is None:
                        print(MyListItem.HeadNode, end = " ")
                        MyListItem = MyListItem.NextItem
        
                print("\n")
