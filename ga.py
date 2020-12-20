# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg
from sklearn import svm
import numpy as np
from sklearn.cluster import KMeans
import plotly.graph_objects as go
import heapq
from PIL import Image
import math
import random
import tensorflow as tf


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def first_population():
    population = []
    for i in range (0, generation_size):
        population.append(get_element())
    parent1 = population[random.randint(0, 4)]
    parent2 = population[random.randint(0, 4)]
    population.append(add_to_population(crossbreeding(parent1, parent2)[0]))
    population.append(add_to_population(crossbreeding(parent1, parent2)[1]))
    population = sorted(population, key=lambda pop: pop[1])
    new_population = []
    for i in range(0, 5):
        new_population.append(population[i])
    return new_population[0][1]


def add_to_population(new_pop):
    arr = new_pop
    distance_sum = 0
    for i in range(1, len(arr)):
        distance_sum = distance_sum + get_distance(df['x'][arr[i]], df['x'][arr[i - 1]], df['y'][arr[i]], df['y'][arr[i - 1]])
    return (arr, distance_sum)


def crossbreeding(parent1, parent2):
    child1 = [parent1[0][0], parent1[0][1]]
    child2 = [parent2[0][0], parent2[0][1]]
    for (p1, p2) in zip(parent1[0], parent2[0]):
        if child1.__contains__(p2) == False:
            child1.append(p2)
        if child2.__contains__(p1) == False:
            child2.append(p1)
    random_mutation_number = random.randint(0, 100)
    if random_mutation_number < mutation_percent:
        child1 = mutation(child1)
    return (child1, child2)


def mutation(child):
    first_random = random.randint(1, 2)
    second_random = random.randint(3, 4)
    child_first_gen = child[first_random]
    child[first_random] = child[second_random]
    child[second_random] = child_first_gen
    return child

def get_element():
    arr = []
    arr.append(0)
    while len(arr) != 5:
        random_number = random.randint(1, 4)
        if arr.__contains__(random_number) == False:
            arr.append(random_number)
    distance_sum = 0
    for i in range(1, len(arr)):
        distance_sum = distance_sum + get_distance(df['x'][arr[i]], df['x'][arr[i-1]], df['y'][arr[i]], df['y'][arr[i-1]])
    return (arr, distance_sum)


# номера городов: 0, 1, 2, 3, 4
# города:
df = pd.DataFrame({
    'x': [5, 19, 24, 38, 44],
    'y': [39, 8, 34, 14, 39]
})
minimum_number = 9999
generation_size = 5
mutation_percent = 10
# количество итераций
iterations = 10
while iterations != 0:
    minimum = first_population()
    if minimum_number > minimum:
        minimum_number = minimum
    iterations = iterations - 1

# минимальная длина путей начиная с первой точки
print(minimum_number)




