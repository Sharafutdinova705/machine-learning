# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches


def read_file_csv(file):
    data = pd.read_csv(file)  # считать файл, данные про титаник
    return data


def build_diagram(dataset):  # отрисовка результата
    count = []
    colors = []
    age = data.Age.head(20)
    p_class = data.Pclass.head(20)
    for i in range(0, len(age)):
        count.append(i + 1)
        if p_class[i] == 1:
            colors.append('g')
        elif p_class[i] == 2:
            colors.append('c')
        else:
            colors.append('y')

    # первый рисунок
    fig = plt.figure(1)
    ax = fig.add_axes([0, 0, 1, 1])
    first_patch = mpatches.Patch(color='g', label='1st passenger class')
    second_patch = mpatches.Patch(color='c', label='2nd passenger class')
    third_patch = mpatches.Patch(color='y', label='3rd passenger class')
    ax.legend(handles=[first_patch, second_patch, third_patch])
    ax.set_xticks(count)

    rects = ax.bar(count, age, color=colors)
    for rect in rects: # для проставления возрастов над каждым баром
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 0), # насколько выше бара находится текст
                    textcoords="offset points",
                    ha='center', # находится относительно центра бара
                    va='bottom')

    # Второй рисунок
    first_class_size = 0
    second_class_size = 0
    third_class_size = 0
    for i in range(0, len(p_class)):
        if p_class[i] == 1:
            first_class_size += 1
        elif p_class[i] == 2:
            second_class_size += 1
        elif p_class[i] == 3:
            third_class_size += 1
    class_names = ['1st class\nCount: ' + str(first_class_size),
                   '2nd class\nCount: ' + str(second_class_size),
                   '3rd class\nCount: ' + str(third_class_size)]
    sizes = [first_class_size, second_class_size, third_class_size]
    fig2 = plt.figure(2)
    ax2 = fig2.add_axes([0, 0, 1, 1])
    ax2.pie(sizes, autopct='%1.1f%%', labels=class_names)
    ax2.axis('equal')  # чтобы получился круг, а не овал
    plt.show()


data = read_file_csv('/Users/guzelsarafutdinova/Desktop/test.csv')
build_diagram(data)
