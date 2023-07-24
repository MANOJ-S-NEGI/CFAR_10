import os
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

load_model = tf.keras.models.load_model("*/saved_model_dir/07_25_2023_01_02_01/20230724-152503_cfar_10_agu_model_2.weights.best.hdf5")
test_file_path = "/*test_image_dir/"


def prediction_pipeline():
    # total number of classification inside test_file_path
    test_file_labels = os.listdir(test_file_path)

    # calling random label folder:
    randum = np.random.choice(test_file_labels)

    # print("actual:", randum)
    # from randum selected folder calling on all images
    image_path = f"{test_file_path}{randum}"
    image_path_file_call = os.listdir(image_path)

    # from image_path randomly calling  select on image:
    randum_image = np.random.choice(range(len(image_path_file_call)))

    # random image:
    image = f"{image_path}/{image_path_file_call[randum_image]}"
    # print image
    image = plt.imread(image)

    image_dimension_expansion = tf.expand_dims(image, axis=0)
    print(image_dimension_expansion.shape)
    pred_image = load_model.predict(image_dimension_expansion)

    # reduced the dimension:
    x = tf.reshape(pred_image, [-1])
    x = tf.argmax(x)
    # predicted label:
    pred_label = test_file_labels[x]

    if pred_label == randum:  # randum is actual_label
        color = "green"
    else:
        color = "red"
    plt.imshow(image)
    plt.title("Prediction: {} \n True_label: {}".format(pred_label, randum), color=color, size=12)
    plt.axis(False);
    plt.show()
