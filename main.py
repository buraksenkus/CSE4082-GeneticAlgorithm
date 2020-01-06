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
    algorithm = GeneticAlgorithm("003.txt", 400, 200, 0.9, 0.05)
    algorithm.run()
