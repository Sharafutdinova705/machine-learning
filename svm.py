# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg
from sklearn import svm
import numpy as np
import sys
from operator import itemgetter, attrgetter, methodcaller


k = 2
colors = {1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 255)}
clusters = []
point_positions = []
pg.init()
screen = pg.display.set_mode((500, 500))
screen.fill((255, 255, 255))

is_running_flag = True

while is_running_flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running_flag = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            point_positions.append(event.pos)
            if event.button == 1:
                pg.draw.circle(screen, colors[1], event.pos, 5)
                clusters.append(0)
            else:
                pg.draw.circle(screen, colors[2], event.pos, 5)
                clusters.append(1)
        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            clf = svm.SVC(kernel='linear', C=1.0)
            clf.fit(point_positions, clusters)
            w = clf.coef_[0]
            n = -w[0] / w[1]
            xx = np.linspace(0, 500, 2)
            yy = n * xx - (clf.intercept_[0]) / w[1]
            pg.draw.line(screen, colors[3], (xx[0], yy[0]), (xx[-1], yy[-1]))
    pg.display.update()
