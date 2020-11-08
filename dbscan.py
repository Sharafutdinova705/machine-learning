
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def show_result():
    for x, y in zip(df['x'], df['y']):
        if clusters[0].__contains__([x, y]):
            plt.scatter(x, y, color=colors[2])
        if clusters[1].__contains__([x, y]):
            plt.scatter(x, y, color=colors[3])
        if clusters[2].__contains__([x, y]):
            plt.scatter(x, y, color=colors[1])
    plt.show()


radius = 10
np.random.seed(158)
df = pd.DataFrame({
    'x': [12, 10, 11, 13, 15, 17, 19, 20, 23, 27, 30, 79, 69, 57, 65, 76, 78, 72, 73, 70, 67, 62, 66, 74, 75, 80, 60, 60, 38, 57, 49, 83, 90, 86, 79, 10, 37, 85],
    'y': [29, 12, 20, 30, 32, 34, 31, 37, 35, 40, 42, 50, 56, 57, 54, 53, 60, 61, 63, 55, 52, 51, 58, 62, 91, 81, 82, 91, 62, 73, 89, 17, 29, 24, 25, 48, 73, 26]
})
colors = {1: 'r', 2: 'g', 3: 'y'}
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
clusters = [[] for _ in range(3)]

plt.xlim(0, 100)
plt.ylim(0, 100)


def fill_clusters():
    global clusters
    clusters = [[] for _ in range(3)]
    zipped = zip(df['x'], df['y'])
    for x, y in zipped:
        count = 0
        for x1, y1 in zipped:
            if [x, y] == [x1, y1]:
                continue
            if get_distance(x1, x, y1, y) < radius:
                count = count + 1
            if count == 3:
                clusters[0].append([x, y])
                break
            if (count < 3) & (x1 == df['x'][len(df['x'])-1]) & (y1 == df['y'][len(df['y'])-1]):
                clusters[2].append([x, y])
    count = 0
    for point in clusters[0]:
        for point1 in clusters[2]:
            if get_distance(point[0], point1[0], point[1], point1[1]) < radius:
                clusters[1].append(point1)
                clusters[2].remove(point1)


show_result()
fill_clusters()
show_result()

print(clusters[0])
print(clusters[1])
print(clusters[2])
