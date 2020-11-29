# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import itemgetter, attrgetter, methodcaller


def get_distance(x1, x2, y1, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def classificate(new_value):
    for brand, price, quality in zip(df['brand'], df['price'], df['quality']):
        distances.append((get_distance(new_value[0], price, new_value[1], quality), brand))
    distances.sort(key=itemgetter(0))
    new_distances = []
    for index in range(0, k-1):
        new_distances.append(distances[index])
    print(new_distances)
    brand0_count = 0
    brand1_count = 0
    for distance, brand in new_distances:
        if brand == 0:
            brand0_count = brand0_count + 1
        elif brand == 1:
            brand1_count = brand1_count + 1
    if brand0_count > brand1_count:
        print("This value is a branded thing")
    else:
        print("This value is a not branded thing")


df = pd.DataFrame({
    'brand': [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    'price': [120, 1999, 1199, 13, 1898, 1787, 19, 2987, 23, 2876, 30, 7923, 6934, 5734, 65, 1976, 76, 7876, 72, 7376, 70, 6765, 62, 6654, 74, 7565, 80, 6065, 60, 3865, 57, 4976, 83, 9065, 86, 7965, 10, 3765, 85],
    'quality': [290, 9909, 9878, 300, 826, 9468, 368, 976, 350, 9068, 426, 9067, 566, 575, 506, 536, 660, 641, 636, 557, 525, 5717, 558, 718, 762, 971, 871, 962, 951, 942, 733, 929, 170, 990, 240, 905, 480, 903, 206]
})
distances = []
k = isqrt(len(df['brand']))
# по цене и качеству классифицируется, брендовая ли вещь
new_value = [5000, 200]
classificate(new_value)
