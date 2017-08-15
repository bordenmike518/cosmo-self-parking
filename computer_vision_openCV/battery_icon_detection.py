import numpy as np
import cv2

battery_icon = cv2.CascadeClassifier('haar_cascades/battery_icon_cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    batteryIcon = battery_icon.detectMultiScale(gray,2,6)

    for (x,y,w,h) in batteryIcon:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print 'x = %.2f y = %.2f' % (x, y)


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
