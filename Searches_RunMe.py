from Class_AdjacencyArray import *
from Module_Fwd_Rev_BreadthandDepth_Searches import *

"""

        Program File to test Topological Sort Algorithm

"""
def main():

        AA = AdjacencyArray()

        AA.GetAdjacencyArray("Network3.dat")

        SNode = "1"

        fbMark, fbPred, fbOrder = FSearchB(SNode, AA)   
                
        print("---------- Network3.dat ------------ \n \n")

        for node in AA.data.keys():
                print("Source ", SNode, " to ", node, " marked: ", fbMark[node], " Pred - ", fbPred[node].Node)

        print(" \n \n")

        


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
