from collections import defaultdict
import csv # Comma Seperated Variable Module
from Class_SinglyLinkedList import *

# Adjacency Array Class
"""     
        This is an attempt at making an Adjacency Array class. I call it an Adjacency Array
        because of convention but really my implementation is a Dict of Singly Linked Lists.
        The names of the nodes with this implementation do not have to be integers, so they can
        be strings or other meaningful means os referencing nodes.

        Attributes:
                .data - Where the actual adjacency data is stored
                .Count - Returns number of nodes in the network

        Methods:
                .GetAdjacencyArray - Loads the data from a Comma Seperated Value (csv) file into the .data attribute
                        Use:
                                AdjacencyArrayObject.GetAdjacencyArray(filename_arg)
                                Where:
                                        filename_arg - comma seperated data file
                .aPrint - Prints the Adjacency Array 
                        Use:
                                AdjacencyArrayObject.aPrint()                         
      
"""    

class AdjacencyArray(object):     
        
        def __init__(self):
                
                self.data = None

                self.Count = 0

        def GetAdjacencyArray(self, Filename_arg):   

                AdjArray_var = defaultdict(SinglyLinkedList) # For Each New Node Make Them a Singly Linked List

                MyFile = open(Filename_arg, "r")   # Open the file read only

                reader = csv.reader(MyFile) # This grabs the data using the comma seperated values function(?)

                for ParsedLine in reader: # Each row is a parsed list      
                        if len(ParsedLine) == 2:                                        
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1]) # .AddItem(HeadNode)
                        elif len(ParsedLine) == 3:                        
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1], int(ParsedLine[2])) # .AddItem(HeadNode, EdgeCost)
                        elif len(ParsedLine) == 4:
                                # .AddItem(HeadNode, EdgeCost, UpperCapacity)
                                AdjArray_var[ParsedLine[0]].AddItem(ParsedLine[1], int(ParsedLine[2]), int(Parsed[3])) 
                        else:                        
                                raise ValueError("Error Data Size in Data File")

                self.data = AdjArray_var   

                self.Count = len(AdjArray_var)  

        def aPrint(self):

                for MyNode in self.data.keys():             
                        print("Node ", MyNode, ": ", end = " ")
                        MyListItem = self.data[MyNode].GetListHead
                        while not MyListItem is None:
                                print(MyListItem.HeadNode, end = " ")
                                MyListItem = MyListItem.NextItem        
                        print("\n")          
