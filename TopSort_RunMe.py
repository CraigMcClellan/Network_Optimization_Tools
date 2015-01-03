from Class_AdjacencyArray import *
from Module_Topological_Sort import *

"""

        Program File to test Topological Sort Algorithm

"""

def main():

        MyArray = AdjacencyArray()

        MyArray.GetAdjacencyArray("Network1.dat")

        Cyclicness, TheOrder = Topological_Sort(MyArray)

        print("Cyclic:= ", Cyclicness, "\n")

        for node in MyArray.data.keys():
                print("Node (",node,"):= ",TheOrder[node], "\n")

        


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main() #main(sys.argv[1])
