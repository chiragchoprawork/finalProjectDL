import tensorflow as tf

# Check available GPU devices.
print("Available GPUs:", tf.test.gpu_device_name())

# Alternatively, list all device kinds and names
from tensorflow.python.client import device_lib
print("All devices:", device_lib.list_local_devices())
