from Class_AdjacencyArray import *
from Module_Fwd_Rev_BreadthandDepth_Searches import *

"""

        Program File to test Topological Sort Algorithm

"""
def main():

        datfile = "Network3.dat"

        AA = AdjacencyArray()

        AA.GetAdjacencyArray(datfile)

        SNode = "1"

        print(" \n ---------- Forward Breadth Search: ", datfile, " ----------- \n")

        fbMark, fbPred, fbOrder = FSearchB(SNode, AA)   

        for node in AA.data.keys():
                print("Source ", SNode, " to ", node, " Marked: ", fbMark[node], " Immediate Pred - ", fbPred[node].Node)

        print(" \n \n")

        print(" \n ---------- Forward Depth Search: ", datfile, " ----------- \n")


        fdMark, fdPred, fdOrder = FSearchD(SNode, AA)   

        for node in AA.data.keys():
                print("Source ", SNode, " to ", node, " Marked: ", fdMark[node], " Immediate Pred - ", fdPred[node].Node)

        print(" \n \n")


        


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
