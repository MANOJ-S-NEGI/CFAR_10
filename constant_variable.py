TRAIN_DIR = "train_path"
VALIDATION_DIR = "validation_filepath"

# generator module constants:

SHEAR_RANGE = 0.2
ZOOM_RANGE = 0.2
HORIZONTAL_FLIP = True
RESCALE = 1 / 255
SHUFFLE = True
TARGET_SIZE = 64
CLASS_MODE = 'categorical'
BATCH_SIZE = 32
VERTICAL_FLIP = True

# TRAINING MODULE CONSTANTS:
KERNEL_SIZE = (3, 3)
PADDING = 'same'
INPUT_SHAPE = (64, 64, 3)
POOL_SIZE = (2, 2)
VERBOSE = 2
SAVE_MODEL_PATH = "saved_model_dir"
SAVED_MODEL_NAME = "_cfar_10_agu_model_2.weights.best.hdf5"
CALLBACK_PATIENCE = 3
EPOCHS = 20
ACTIVATION = "LeakyReLU"
FINAL_ACTIVATION = "softmax"
OPTIMIZER = "adam"
LOSS = 'categorical_crossentropy'
METRICS = ["accuracy"]
