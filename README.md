# Attendance-system-using-Facial-Recognition
![Face-Recognition-in-Python](https://user-images.githubusercontent.com/83969166/211626687-0ea2af05-68c6-46a8-914d-18bcbe9c28e6.jpg)

# Installing libraries
open cv
```python
pip install opencv-python
```
Facial Recognition
```python
pip install face-recognition
```
Numpy
```python
pip install numpy
```

#OpenCV 

```python
import cv2
import os

#cv2.imread()
path = os.getcwd() 
img = cv2.imread(path)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
success, img = cap.read()
cv2.imshow('Webcam', img)
cv2.waitKey(5000)
cv2.imwrite(filename, img)
```
