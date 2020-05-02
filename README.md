# File-Vault
A file locker with application with Face-lock.

## Description
A simple file locker with python using Tkinter for GUI.\
User can login using username & password and then set facelock. File locking is easy. Just press the 'Lock File' button select the file. The file is encrypted using **AES**. User can unlock the file by clicking button. File will be decrypted automatically. Face lock can be set and reset by pressing the facelock icon.

## Dataset
http://vis-www.cs.umass.edu/lfw/

## How Does Is Work
OpenCV, Keras, Tensorflow is used to make the face verification module. LFW dataset (link is given below). The dataset is processed and saved in the Dataset folder. Dataset processing required croping face form the image, resize it.\
OpenCV's Haar-cascade frontal face classifier is used to crop the face. It is also used while verifying face in realtime.\
Siamese CNN, Triplet loss function is used to build the classifier. **VGG16** pre-trained model is used. The VGG16 model is converted to a **Siamese Convolutional Neural Network** with **Triplet Loss** as loss function for **one shot learning**. This process is called **Transfer Learning**.
The model is saved as a .h5 file for further use.

## Testing Instruciton
Run **Lock.py** to test. **Train.ipynb** notebook shows the siamese model creation, triplet loss function and the training session.
**tripletmodelVGG.h5** is  the saved model after training. 
  


**Sorry for my bad writing**
