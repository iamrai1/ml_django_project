from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import pickle
import cv2
def prediction (model, labelbin, image):
    args = [model, labelbin, image]
    # load the image
    image = cv2.imread(args[2])
    # output = image.copy()

    # pre-process the image for classification
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load the trained convolutional neural network and the label
    # binarizer
    # print("[INFO] loading network...")
    model = load_model(args[0])
    lb = pickle.loads(open(args[1], "rb").read())
    # classify the input image
    # print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    return label
