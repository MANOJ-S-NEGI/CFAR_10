# DATASET: CFAR_10 [Image Classification]
### DATE: 2023 JUNE
### Program Language: Python

>>Dataset Description:
```
* The CFAR-10 data consists of 50,000 32x32 color images in 10 classes, with 5000 images per class.
* There are 50,000 training images and 10,000 test images in the official data.


The label classes in the dataset are:

* airplane
* automobile
* bird
* cat
* deer
* dog
* frog
* horse
* ship
* truck

The classes are completely mutually exclusive. There is no overlap between automobiles and trucks.
 "Automobile" includes sedans, SUVs, and things of that sort. "Truck" includes only big trucks. Neither includes pickup trucks.
```

### Project Description:
```
1. Programming Language used: python
2. For Results web framework used:  FastAPI

the dataset contains 50000 images of each class mentioned above as a label class for the training of the model.
the model saved on the best weights with a validation accuracy of 74% as plotted.
trained model weights are attached in saved_model_dir.
```
![model2_cfar_plot](https://github.com/MANOJ-S-NEGI/CFAR_10/assets/99602627/9d20d4a2-9df9-4811-8f74-d947ee697411)


```
Setup:
* Create a virtual environment
* Run requirements.txt as pip install -r requirements.txt

Note:
if the directory is not found an error occurs
* set the test_image_dir path and saved_model_path in prediction.py
* run main.py


>> Run main.py then Copy the URL  http://127.0.0.1:8000/docs to check the predictions
```
### result will plot as:
![Figure_1](https://github.com/MANOJ-S-NEGI/CFAR_10/assets/99602627/f285fd8b-1799-4dc8-9fc9-6720b396bc0d)


