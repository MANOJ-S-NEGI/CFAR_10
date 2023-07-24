import tensorflow as tf
from Model_folder.ingestion_module import DataIngestionTraining
import log_file as logging
from  constant_variable import *
import os
from datetime import datetime
import logging


class TrainingConfig:
    def __init__(self):
        self.train_data = DataIngestionTraining().Train_DataGenerator()
        self.validation_data = DataIngestionTraining().Validation_DataGenerator()

    @staticmethod
    def Model_Layer():
        try:
            logging.info("Initialising the model layering")

            model_2 = tf.keras.Sequential([
                tf.keras.layers.Conv2D(32, kernel_size=KERNEL_SIZE, padding=PADDING,activation=ACTIVATION, input_shape=INPUT_SHAPE),
                tf.keras.layers.MaxPooling2D(pool_size=POOL_SIZE),
                tf.keras.layers.Conv2D(64, kernel_size=KERNEL_SIZE, padding=PADDING, activation=ACTIVATION),
                tf.keras.layers.MaxPooling2D(pool_size=POOL_SIZE),
                tf.keras.layers.Conv2D(128, kernel_size=KERNEL_SIZE, padding=PADDING, activation=ACTIVATION),
                tf.keras.layers.MaxPooling2D(pool_size=POOL_SIZE),
                tf.keras.layers.Conv2D(256, kernel_size=KERNEL_SIZE, padding=PADDING, activation=ACTIVATION),
                tf.keras.layers.MaxPooling2D(pool_size=POOL_SIZE),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(10, activation=FINAL_ACTIVATION),
            ])

            model_2.summary()
            return model_2
        except Exception as e:
            raise Exception("error in layer function ", str(e))

    @staticmethod
    def callbacks():
        try:
            logging.info("initialising the callback functions")
            # Setting the Callback Function -
            # Create a function to implement a ModelCheckpoint callback with a specific filename

            timestamp = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
            saved_model_directory = os.path.join(SAVE_MODEL_PATH, timestamp)
            os.makedirs(saved_model_directory, exist_ok=True)
            filepath = f"{saved_model_directory}/{SAVED_MODEL_NAME}"

            savepointer = tf.keras.callbacks.ModelCheckpoint(filepath=filepath, verbose=VERBOSE, save_best_only=True)

            # Create a function to implement an Early stop callback with loss monitor
            Early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                          patience=CALLBACK_PATIENCE,
                                                          verbose=VERBOSE)
            callbacks = [savepointer, Early_stop]
            return callbacks

        except Exception as e:
            raise Exception("error in callback function ", str(e))

    def model_compile_training(self):
        try:
            model_layers = TrainingConfig.Model_Layer()
            callbacks = TrainingConfig.callbacks()

            logging.info("compiling model")
            model_layers.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRICS)
            logging.info("model compilation done")

            logging.info("initializing the model fitting/training")

            model_layers.fit(self.train_data,
                             validation_data=self.validation_data,
                             validation_steps=int(len(self.validation_data)),
                             steps_per_epoch=int(len(self.train_data)),
                             batch_size=BATCH_SIZE,
                             epochs=EPOCHS,
                             callbacks=callbacks)
            logging.info("model with trainable bias saved")

        except Exception as e:
            raise ("error in model_compile_training function", e)


print(TrainingConfig().model_compile_training())
