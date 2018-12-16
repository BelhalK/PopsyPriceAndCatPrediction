Testing the CNN
========================================================

Code in this directory focuses on how to make prediction of the category and the price range given an image:

Before trying to run the model we highly encourage you to read all the README.

## Prerequisite

1. [Install](https://www.tensorflow.org/install/) TensorFlow version 1.2.1 or
later.
2. Keras
3. opencv-python
4. pickle

## Content:
1. model: Folder with the trained model

2. pickle: label for parent categories (9) and price ranges (4 per category)

3. classify.py: to predict categories and price ranges


## Usage:

To try your model and predict category and price range given a new image you can run:
```
python3 classify.py --model model/popsy.model --categorybin pickle/category_lb.pickle --pricebin pickle/price_lb.pickle  --image dataset/testset/<your_image>.jpg
```