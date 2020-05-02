import cv2
import keras
from fr_utils import *


def triplet_loss(y_true, y_pred, alpha=0.5):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
    return loss


THRESHOLD = 0.0025
IMG_SIZE = 224


def load():
    global FRmodel
    FRmodel = keras.models.load_model('tripletmodelVGG.h5', custom_objects={'triplet_loss': triplet_loss})
    img = cv2.imread('Images\mainface.jpg')
    cv2.imshow('reference',img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    global reference
    reference = img_to_encoding(img, FRmodel)

def verify(image):
    encoding = img_to_encoding(image, FRmodel)
    global reference
    dist = np.linalg.norm(encoding - reference)
    if dist < THRESHOLD:
        matched = True
    else:
        matched = False
    return dist, matched


def capture(capture_only=False):
    if not capture_only:
        load()
    cam = cv2.VideoCapture(0)
    it=0
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        ret, frame = cam.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray=frame.copy()
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        frame_copy = gray.copy()
        # if len(faces) > 1:
        #    print("Multiple face detected. One is needed")
        # else:
        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = frame_copy[y:y + h, x:x + w]
            cv2.imshow('face ', face)
            if capture_only:
                cv2.imwrite('Images/mainface.jpg', face)
                cam.release()
                cv2.destroyAllWindows()
                return
            else:
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (IMG_SIZE, IMG_SIZE))
                dist, detected = verify(face)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if detected == True:
                    cv2.putText(frame, 'Detected ' + str(dist), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255),
                                lineType=cv2.LINE_AA)
                    cam.release()
                    cv2.destroyAllWindows()
                    return True
                else:
                    cv2.putText(frame, str(dist), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                (255, 0, 0),
                                lineType=cv2.LINE_AA)
                    it=it+1
                    if it>25:
                        cam.release()
                        cv2.destroyAllWindows()
                        return False
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture()
