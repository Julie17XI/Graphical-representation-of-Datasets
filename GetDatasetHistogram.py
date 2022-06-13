import os
from collections import defaultdict
from itertools import repeat
import  matplotlib.pyplot as plt

def getAges(dataset_folder):
    '''Count the number of images for each age'''
    ages = defaultdict(lambda: 0)
    for fileName in os.listdir(dataset_folder):
        age = int(fileName.split('_')[0])
        ages[age] += 1
    ages = sorted(ages.items(), key = lambda item : item[0])
    return dict(ages)

def getTotalNumOfImages(dict):
    return sum(dict.values())

def makeEmptyBins():
    '''Make a dictionary that sets value 0 to age 0-100'''
    bins = dict(zip(range(101), repeat(0)))
    return bins

def populateBins(age_counter, bins):
    bins.update(age_counter)
    return bins

def plotHistogram(dataset, ages, total_num_images):
    plt.bar(ages.keys(), ages.values())
    plt.xlabel('Age')
    plt.ylabel('Number of people')
    plt.title(f"{dataset} Data distribution")
    plt.grid(axis='y', alpha=0.75)
    plt.text(70,235, f'Total number = {total_num_images}')
    plt.show()
    return

#
# Start of main
#

# Get graphical representations for custom datasets
# dataset_folder = "./StevenOHara"
# ages = getAges(dataset_folder)
# total_num_images = getTotalNumOfImages(ages)
# bins = makeEmptyBins()
# populate_bins = populateBins(ages, bins)
# plotHistogram('OneIndividual', populate_bins, total_num_images)

# Get graphical representations for benchmark datasets
