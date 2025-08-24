import numpy as np
import pandas as pd
import os

from sklearn.model_selection import train_test_split
import random
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical

import tensorflow as tf
print(tf.__version__)