# genetic algorithm

import random
import datetime

# Definition of the gene set (possible characters) and target phrase
geneSet = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!."
target = "Hello World!"

# Helper function : Create a random parent (initial candidate solution) of a given length
def createParent(length):
    genes=[]
    while len(genes)<length:
        sampleLength = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleLength))
    return "".join(genes)

# Helper function : Calculate the fitness (number of correct characters) of a given forecast
def fitness(forecast):
    return sum(1 for predicted, realized in zip(target, forecast) if predicted == realized)

# Helper function : Perform a mutation on a given parent to create a child
def mutation(parent):
    index = random.randrange(0, len(parent))
    childrenGenes = list(parent)
    newGene, progress = random.sample(geneSet, 2)
    childrenGenes[index] = progress if newGene == childrenGenes[index] else newGene
    return "".join(childrenGenes)

# Helper function : Display all the forecast, fitness, and time passed
def display(forecast):
    timePassed = datetime.datetime.now() - startTime
    fitnessValue = fitness(forecast)
    print("{0}\t{1}\t{2}".format(forecast, fitnessValue, str(timePassed)))


## Run !

# Initialize the random number generator and starting time
random.seed()
startTime = datetime.datetime.now()

# Create the initial parent and best fitness value
bestParent = createParent(len(target))
bestFitnessValue = fitness(bestParent)
display(bestParent)

# Iterate until a solution is found
while True:
    child = mutation(bestParent)
    childFitnessValue = fitness(child)

    # Only update the best parent if the child is fitter
    if bestFitnessValue >= childFitnessValue:
        continue
    display(child)
    if childFitnessValue >= len(bestParent):
        break
    bestFitnessValue = childFitnessValue
    bestParent = child