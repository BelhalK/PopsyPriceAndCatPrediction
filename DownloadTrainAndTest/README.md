Downloading datasets using BigQuery and Training the CNN
========================================================

Code in this directory focuses on how to use create and download your training and testing dataset.

Before trying to run the model we highly encourage you to read all the README.

## Prerequisite

1. [Install](https://www.tensorflow.org/install/) TensorFlow version 1.2.1 or
later.

2. Install Google cloud python package 

3. Install forex-python package for currency

3. Install pathlib package


## Content:
1. dataset: Folder with the scripts allowing you to download images using BigQuery API and order them in labelled folder (for training purposes)

2. pyimagesearch: Folder with the CNN

3. output: Folder with the outputs of the training phase i.e. the losses (png) and the serializer (labels)

4. train.py: to train your CNN
5. classify.py: to predict categories and price ranges


## Workflow:

First authenticate to your database using your json file entering in your terminal 
```
export GOOGLE_APPLICATION_CREDENTIALS=<your_path_with_key>/yourjsonfile.json
```
Then set up your sql folder in which all your queries are.

You can now run 
```
python createdir.py --queries sql/
```
this script will create training (80% of the data) and testing (20% of the data) sets ordered in categories and price ranges (for now percentiles 25, 50, 75 and 100)

NB: 
```
python remove.py
```
can delete those directories.
Now you can run 
```
python run.py --queries sql/
```
This will fill your pre created folders for training and testing.


Finally, 
```
python train.py --dataset dataset/trainset --model output/popsy.model --categorybin output/category_lb.pickle --pricebin output/price_lb.pickle
```
will train your model.

To try your model and predict category and price range given a new image you can run:
```
python3 classify.py --model output/popsy.model --categorybin output/category_lb.pickle --pricebin output/price_lb.pickle  --image dataset/testset/<your_image>.jpg
```