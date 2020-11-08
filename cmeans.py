# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_membership_coefficient(dist):
    return (1/dist)**(2/(coefficient-1))


def get_average(centers):
    cluster_mean_ax = 0
    cluster_mean_bx = 0
    cluster_mean_ay = 0
    cluster_mean_by = 0
    for index, membership_coefficient in enumerate(membership_coefficients_to_center_1):
        cluster_mean_ax = cluster_mean_ax + (membership_coefficient**coefficient)
        cluster_mean_bx = cluster_mean_bx + (membership_coefficient**coefficient) * df['x'][index]
        cluster_mean_ay = cluster_mean_ay + (membership_coefficient**coefficient)
        cluster_mean_by = cluster_mean_by + (membership_coefficient**coefficient) * df['y'][index]
    centers[1] = [cluster_mean_bx/cluster_mean_ax, cluster_mean_by/cluster_mean_ay]

    cluster_mean_ax = 0
    cluster_mean_bx = 0
    cluster_mean_ay = 0
    cluster_mean_by = 0
    for index, membership_coefficient in enumerate(membership_coefficients_to_center_2):
        cluster_mean_ax = cluster_mean_ax + (membership_coefficient ** coefficient)
        cluster_mean_bx = cluster_mean_bx + (membership_coefficient ** coefficient) * df['x'][index]
        cluster_mean_ay = cluster_mean_ay + (membership_coefficient ** coefficient)
        cluster_mean_by = cluster_mean_by + (membership_coefficient ** coefficient) * df['y'][index]
    centers[2] = [cluster_mean_bx / cluster_mean_ax, cluster_mean_by / cluster_mean_ay]
    return centers


def show_result():
    for i in centers.keys():
        plt.scatter(*centers[i], color=colors[i])
    for j, f, s in zip(range(len(df['x'])), membership_coefficients_to_center_1, membership_coefficients_to_center_2):
        if f > s:
            plt.scatter(df['x'][j], df['y'][j], color=colors[1])
        else:
            plt.scatter(df['x'][j], df['y'][j], color=colors[2])
    plt.show()

k = 2
coefficient = 0.2
eps = 0.3
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

membership_coefficients_to_center_1 = []
membership_coefficients_to_center_2 = []

def fill_clusters():
    global clusters
    clusters = [[] for _ in range(k)]
    distances_to_center_1 = []
    distances_to_center_2 = []
    global membership_coefficients_to_center_1
    global membership_coefficients_to_center_2
    membership_coefficients_to_center_1 = []
    membership_coefficients_to_center_2 = []
    sum = 0

    for i, j in zip(df['x'], df['y']):
        distances_to_center_1.append(get_distance(i, centers[1][0], j, centers[1][1]))
        distances_to_center_2.append(get_distance(i, centers[2][0], j, centers[2][1]))

    for distance_to_center_1, distance_to_center_2 in zip(distances_to_center_1, distances_to_center_2):
        membership_coefficient_to_center_1 = get_membership_coefficient(distance_to_center_1)
        membership_coefficient_to_center_2 = get_membership_coefficient(distance_to_center_2)
        membership_coefficients_to_center_1.append(membership_coefficient_to_center_1/(membership_coefficient_to_center_1+membership_coefficient_to_center_2))
        membership_coefficients_to_center_2.append(membership_coefficient_to_center_2/(membership_coefficient_to_center_1+membership_coefficient_to_center_2))

    for i in range(len(distances_to_center_1)):
        sum = sum + ((distances_to_center_1[i] * membership_coefficients_to_center_1[i]) + (distances_to_center_2[i] * membership_coefficients_to_center_2[i]))

    return sum


count = 0
sum = 0
show_result()
while(True):
    old_sum = sum
    sum = fill_clusters()
    print(centers)
    old_centers = centers.copy()
    print(old_centers)
    new_centers = get_average(centers).copy()
    print(new_centers)
    centers = new_centers.copy()
    print(old_centers)
    print(old_sum)
    print (sum)
    print(eps)
    if abs(old_sum - sum) < eps:
        print("Count of iterations: ", count)
        break
    show_result()
    count = count + 1
