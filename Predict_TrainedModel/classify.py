# USAGE
# python3 classify.py --model model/popsy.model \
#	--categorybin pickle/category_lb.pickle --pricebin pickle/price_lb.pickle \
#	--image path/to/image

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import tensorflow as tf
import numpy as np
import argparse
import imutils
import pickle
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--categorybin", required=True,
	help="path to output category label binarizer")
ap.add_argument("-c", "--pricebin", required=True,
	help="path to output price label binarizer")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
output = imutils.resize(image, width=400)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# pre-process the image for classification
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network from disk, followed
# by the category and price label binarizers, respectively
print("[INFO] loading network...")
model = load_model(args["model"], custom_objects={"tf": tf})

categoryLB = pickle.loads(open(args["categorybin"], "rb").read())
priceLB = pickle.loads(open(args["pricebin"], "rb").read())

# categoryLB = pickle.loads(open("category_lb.pickle", "rb").read())

# classify the input image using Keras' multi-output functionality
print("[INFO] classifying image...")
(categoryProba, priceProba) = model.predict(image)

# find indexes of both the category and price outputs with the
# largest probabilities, then determine the corresponding class
# labels
categoryIdx = categoryProba[0].argmax()
priceIdx = priceProba[0].argmax()
categoryLabel = categoryLB.classes_[categoryIdx]
priceLabel = priceLB.classes_[priceIdx]

# draw the category label and price label on the image
categoryText = "category: {} ({:.2f}%)".format(categoryLabel,
	categoryProba[0][categoryIdx] * 100)
priceText = "price: {} ({:.2f}%)".format(priceLabel,
	priceProba[0][priceIdx] * 100)
cv2.putText(output, categoryText, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)
cv2.putText(output, priceText, (10, 55), cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

# display the predictions to the terminal as well
print("[INFO] {}".format(categoryText))
print("[INFO] {}".format(priceText))

# show the output image
cv2.imshow("Output", output)
cv2.waitKey(0)