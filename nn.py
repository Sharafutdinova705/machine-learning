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

import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x_train, y_train, epochs=5)
test_loss, test_acc = model.evaluate(x_test, y_test)

print('\n Accuracy:', test_acc)

FPS = 60
pg.init()
w=300
h=300
WHITE = (255,255,255)
BLACK = (0,0,0)
sc = pg.display.set_mode((w,h))
sc.fill(BLACK)
clock = pg.time.Clock()
flag = False
pg.display.update()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.image.save(sc, "pic.jpg")
            img = Image.open('./pic.jpg')
            img = img.resize((28, 28))
            img = img.convert('L')
            img = np.array(img)
            img = img / 255.0
            img_arr = np.expand_dims(img, axis=0)

            result = model.predict_classes(img_arr, 28, 1)
            print(result)

            exit()

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            flag = True
            pos = pg.mouse.get_pos()
            pg.draw.circle(sc, WHITE, pos, 12)
            pg.display.update()

        elif event.type == pg.MOUSEMOTION:
            if flag:
                pg.draw.circle(sc, WHITE, event.pos, 12)
                pg.display.update()

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            flag = False

    clock.tick(FPS)
