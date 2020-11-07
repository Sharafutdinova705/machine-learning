# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_average(clusters):
    for i, cluster in enumerate(clusters):
        cluster_mean_x = np.mean(df['x'][cluster], axis=0)
        cluster_mean_y = np.mean(df['y'][cluster], axis=0)
        centers[i+1] = [cluster_mean_x, cluster_mean_y]
    return centers


def show_result():
    for i in centers.keys():
        plt.scatter(*centers[i], color=colors[i])
    for j in range(len(df['x'])):
        for i, index in zip(clusters, range(len(clusters))):
            if i.__contains__(j):
                plt.scatter(df['x'][j], df['y'][j], color=colors[index + 1])
    plt.show()

k = 3
np.random.seed(158)
df = pd.DataFrame({
    'x': [12, 10, 11, 13, 15, 17, 19, 20, 23, 27, 30, 79, 69, 57, 65, 76, 78, 72, 73, 70, 67, 62, 66, 74, 75, 80, 60, 60, 38, 57, 49, 83, 90, 86, 79, 10, 37, 85],
    'y': [29, 12, 20, 30, 32, 34, 31, 37, 35, 40, 42, 50, 56, 57, 54, 53, 60, 61, 63, 55, 52, 51, 58, 62, 91, 81, 82, 91, 62, 73, 89, 17, 29, 24, 25, 48, 73, 26]
})
centers = {
    i+1: [np.random.randint(0, 100), np.random.randint(0, 100)]
    for i in range(k)
}
colors = {1: 'r', 2: 'g', 3: 'b'}
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
clusters = [[] for _ in range(k)]

plt.xlim(0, 100)
plt.ylim(0, 100)


def fill_clusters():
    global clusters
    clusters = [[] for _ in range(k)]
    distances_to_center_1 = []
    distances_to_center_2 = []
    distances_to_center_3 = []

    for i, j in zip(df['x'], df['y']):
        distances_to_center_1.append(get_distance(i, centers[1][0], j, centers[1][1]))
        distances_to_center_2.append(get_distance(i, centers[2][0], j, centers[2][1]))
        distances_to_center_3.append(get_distance(i, centers[3][0], j, centers[3][1]))

    for i in range(len(distances_to_center_1)):
        min_dist = distances_to_center_1[i]
        min_index = 1
        if distances_to_center_2[i] < min_dist:
            min_dist = distances_to_center_2[i]
            min_index = 2
        if distances_to_center_3[i] < min_dist:
            min_dist = distances_to_center_3[i]
            min_index = 3

        clusters[min_index - 1].append(i)

while(True):
    fill_clusters()
    old_centers = centers.copy()
    new_centers = get_average(clusters)
    centers = new_centers
    print(new_centers)
    print(old_centers)
    print(clusters)
    show_result()
    if old_centers == new_centers:
        break
