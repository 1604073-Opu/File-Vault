import os
import shutil
from tqdm import tqdm
import cv2
import numpy as np
import pickle

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
IMAGE_SIZE = 96


def find_face(img):
    gray = img.copy()
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (IMAGE_SIZE, IMAGE_SIZE))
        return True, face
    return False, gray


def cleanImages(findFace=True):
    for folder in os.listdir('Dataset'):
        folder = os.path.join('Dataset', folder)
        if len(os.listdir(folder)) < 3:
            shutil.rmtree(folder)
            continue
        if findFace:
            for img_path in os.listdir(folder):
                img_path = os.path.join(folder, img_path)
                img = cv2.imread(img_path)
                flag, face = find_face(img)
                os.remove(img_path)
                if flag:
                    cv2.imwrite(img_path, face)


#cleanImages(findFace=True)
cleanImages(findFace=False)
input_shape = (3, IMAGE_SIZE, IMAGE_SIZE)
faces = []
images = {}
folders = os.listdir('Dataset')
length = len(folders)
length = 10
for folder_indx in tqdm(range(length)):
    folder = os.path.join('Dataset', folders[folder_indx])
    li = []
    key = ''
    for img in os.listdir(folder):
        key = img
        img1 = cv2.imread(os.path.join(folder, img))
        #img2 = img1[..., ::-1]
        cv2.imshow('img1',img1)
        cv2.imshow('img',np.around(img1 / 255.0, decimals=12))
        cv2.waitKey(0)
        li.append(np.around(np.transpose(img2, (2, 0, 1)) / 255.0, decimals=12))
    images[key] = np.array(li)
    faces.append(key)


def batch_generator(batch_size=16):
    y_val = np.zeros((batch_size, 2, 1))
    anchors = np.zeros((batch_size, input_shape[0], input_shape[1], input_shape[2]))
    positives = np.zeros((batch_size, input_shape[0], input_shape[1], input_shape[2]))
    negatives = np.zeros((batch_size, input_shape[0], input_shape[1], input_shape[2]))
    TOTAL_SIZE = 0
    while True:
        for i in range(batch_size):
            positiveFace = faces[np.random.randint(len(faces))]
            negativeFace = faces[np.random.randint(len(faces))]
            while positiveFace == negativeFace:
                negativeFace = faces[np.random.randint(len(faces))]

            positives[i] = images[positiveFace][np.random.randint(len(images[positiveFace]))]
            anchors[i] = images[positiveFace][np.random.randint(len(images[positiveFace]))]
            negatives[i] = images[negativeFace][np.random.randint(len(images[negativeFace]))]

        x_data = {'anchor': anchors,
                  'anchorPositive': positives,
                  'anchorNegative': negatives
                  }
        yield (x_data, [y_val, y_val, y_val])
