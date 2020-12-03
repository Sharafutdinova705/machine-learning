# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg
from sklearn import svm
import numpy as np
from sklearn.cluster import KMeans
import plotly.graph_objects as go


def get_zz(x, y):
    return (-clf.intercept_[0] - w[0] * x - w[1] * y) / w[2]


k = 50
positions = {
    i: []
    for i in range(3)
}

for i in range(3):
    for j in range(k):
        positions[i].append(np.random.randint(0, k))

print(positions)

points = []
colors = []

for i in range(k):
    points.append([positions[0][i], positions[1][i], positions[2][i]])

clusters = KMeans(n_clusters=2, random_state=0).fit(points).labels_

for i in range(k):
    if clusters[i] == 1:
        colors.append('green')
    else:
        colors.append('red')


clf = svm.SVC(kernel='linear')
clf.fit(points[:], clusters)
w = clf.coef_[0]
temp = np.linspace(0, 50, 50)
xx, yx = np.meshgrid(temp, temp)
fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=positions[0],
    y=positions[1],
    z=positions[2],
    mode='markers',
    marker=dict(color=colors)
))
fig.add_trace(go.Surface(
    x=xx,
    y=yx,
    z=get_zz(xx, yx)
))
fig.show()
