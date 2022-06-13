import os
import csv
from collections import defaultdict
from itertools import repeat
import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#
# Plot custom data distribution
#
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
# Plot UTKFace data distribution
#

def mapRace(index):
    raceMap = {'0': 'caucasian', '1': 'afroamerican', '2': 'asian', '3': 'indian', '4': 'others'}
    return raceMap[index]

def writeUTKDatacsv(UTKFace_dataset_folder):
    with open ('./UTKData.csv', mode='w') as csv_file:
        field_names = ['age', 'gender', 'race', 'dir', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        writer.writeheader()
        for file_name in os.listdir(UTKFace_dataset_folder):
            if file_name == '.DS_Store':
                continue
            print(f"file_name: {file_name.split('_')}")
            age, gender, race, rest = file_name.split('_')
            race = mapRace(race)
            print(f"race: {race}")
            file_path = os.path.join(UTKFace_dataset_folder, file_name)
            writer.writerow({'age': age, 'gender': gender, 'race': race, 'dir': file_path, 'count': 1})
    return

def getNumOfPeopleByRaceAndAge(csv_file):
    data = pd.read_csv(csv_file)
    total_num_people = len(data)
    data.head()
    agg_age_race_counter = data.groupby(['age', 'race'])['count'].sum().unstack().fillna(0)
    agg_age_race_counter.plot(xlabel='Age', ylabel='Number of people', xticks=(np.arange(0, 120, step=10)), kind='bar', stacked=True)
    plt.text(70,1000, f'Total number = {total_num_people}')
    plt.title('UTKFace Data Distribution')
    plt.show()

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

# getNumOfPeopleByRaceAndAge('./UTKData.csv')
