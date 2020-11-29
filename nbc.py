# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import itemgetter, attrgetter, methodcaller


# 0 -  большой
# 1 -  быстрый
# 2 -  высокий прыжок
df = pd.DataFrame({
    'fish': [100, 300, 10],  # всего 400
    'turtle': [300, 0, 0],  # всего 300
    'kangaroo': [300, 150, 300]  # всего 300
    # 700, 650, 310, всего - 1000
})


def classificate(value):
    fish_data = ((df['fish'][0] if value[0] else 400.0-df['fish'][0])/400.0) * ((df['fish'][1] if value[1] else 400.0-df['fish'][1])/400.0) * ((df['fish'][2] if value[2] else 400.0-df['fish'][2])/400.0) * (400.0/1000.0)
    turtle_data = ((df['turtle'][0] if value[0] else 400.0-df['turtle'][0])/300.0) * ((df['turtle'][1] if value[1] else 400.0-df['turtle'][1])/300.0) * ((df['turtle'][2] if value[2] else 400.0-df['turtle'][2])/300.0) * (300.0/1000.0)
    kangaroo_data = ((df['kangaroo'][0] if value[0] else 400.0-df['kangaroo'][0])/300.0) * ((df['kangaroo'][1] if value[1] else 400.0-df['kangaroo'][1])/300.0) * ((df['kangaroo'][2] if value[2] else 400.0-df['kangaroo'][2])/300.0) * (300.0/1000.0)
    if (fish_data > turtle_data) & (fish_data > kangaroo_data):
        print("It's fish")
    elif (turtle_data > fish_data) & (turtle_data > kangaroo_data):
        print("It's turtle")
    elif (kangaroo_data > turtle_data) & (kangaroo_data > fish_data):
        print("It's kangaroo")
    else:
        print("Didn't recognize")

new_value = (True, False, False) # turtle
classificate(new_value)
