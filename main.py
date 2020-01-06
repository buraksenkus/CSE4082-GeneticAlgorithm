from GeneticAlgorithm import GeneticAlgorithm
import sys

if len(sys.argv) == 6:
    try:
        algorithm = GeneticAlgorithm(sys.argv[1], int(sys.argv[2]), int(sys.argv[2]), float(sys.argv[2]), float(sys.argv[2]))
        algorithm.run()
    except ValueError:
        print("Your inputs are invalid. Please correct them. (Use \".\" for floats)")
        exit(0)
else:
    algorithm = GeneticAlgorithm("003.txt", 5, 5, 0.8, 0.1)
    algorithm.run()
