import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone

# Initialize webcam capture
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# Load background image
imgBackground = cv2.imread('Resources/background.png')

# importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))

#load the encoding file
print("LOADING ENCODE FILE...")
file = open('EncodeFile.p','rb')
encodeListKnownIds = pickle.load(file)
file.close()
encodeListKnown , studentIds= encodeListKnownIds
# print(studentIds)
print("ENCODE FILE LOADED")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    #make our image smaller as it will reduce the computational power
    imgS = cv2.resize(img,(0,0),None , 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    #next we need face and encoding of the current frame
    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS,faceCurrentFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    #matching the current with our stored or previous encodings
    #zip method is used to iterate over both the lists
    for encodeFace , faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print("Matches" , matches)
        # print("Face Distance" ,faceDis)

        #getting the index of least value as it is the best match of the face
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            print("KNOWN FACE DETECTED AT THE INDEX ", matchIndex)
            print(studentIds[matchIndex])

            # Scale the face location back to the original size
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox=bbox, rt=0)




    # cv2.imshow("WEB CAM" , img)

    cv2.imshow("Face Attendance",imgBackground)
    cv2.waitKey(1)


