# -*- coding: utf-8 -*-
import os
import cv2 as cv


green = (0, 255, 0)
face_cascade = cv.CascadeClassifier(os.path.abspath('/Users/guzelsarafutdinova/Desktop/haarcascade_frontalface_alt.xml'))
for file in os.listdir('/Users/guzelsarafutdinova/Desktop'):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.jpg':
        image = cv.imread('/Users/guzelsarafutdinova/Desktop/' + file)
        faces = face_cascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            x2, y2 = x + w, y + h
            cv.rectangle(image, (x, y), (x2, y2), green, 2)
        cv.imshow("Face", image)
        cv.waitKey(0)
        cv.destroyAllWindows()
