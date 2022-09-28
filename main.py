import cv2
import numpy as np
import face_recognition

imgryan = face_recognition.load_image_file('IMAGES/ryan.jpg')
imgryan = cv2.cvtColor(imgryan,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('IMAGES/ryantest.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

imgana = face_recognition.load_image_file('IMAGES/ana.jpg')
imgana = cv2.cvtColor(imgana,cv2.COLOR_BGR2RGB)
imganatest = face_recognition.load_image_file('IMAGES/ana test.jpg')
imganatest = cv2.cvtColor(imganatest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgryan)[0]
encoderyan = face_recognition.face_encodings(imgryan)[0]
cv2.rectangle(imgryan,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)



faceloctest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)
results = face_recognition.compare_faces([encoderyan],encodetest)
facedis =face_recognition.face_distance([encoderyan],encodetest)
cv2.putText(imgtest,f'{results} {round(facedis[0],2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,0.5, (0,0,255),1)


print (results,facedis)


cv2.imshow('Ryan reynolds', imgryan)
cv2.imshow('Ryan Test',imgtest)
cv2.waitKey(0)