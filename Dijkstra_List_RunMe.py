from Module_Dijkstras_ShortestPathAlgorithm_List import *
from Class_SinglyLinkedList import *
from Class_AdjacencyArray import *
from collections import defaultdict
import csv # Comma Seperated Variable Module

"""     Run File to solve an example Network using Dijkstra's Shortest Path Algothim 
        implementing Singly Linked Lists and my Adjacency Array Class.  This is the 
        least efficient implementation """        

def main():
        

        XArray = AdjacencyArray()

        XArray.GetAdjacencyArray('Network2.dat')

        #XArray.aPrint()

        #print("Count :=", XArray.Count)

        print("\n \n")

        MySourceNode = "8"

        Dist_Array, Pred_Array = SPA_Dijkstra(MySourceNode, XArray)

        print("----------- Results ---------- \n \n")
        for node in XArray.data.keys():
                print("From Source Node ", MySourceNode," to Node(", node, ") - Dist:", Dist_Array[node]," Pred:", Pred_Array[node])
   


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
