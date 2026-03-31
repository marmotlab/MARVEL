"""
Configuration parameters for MARVEL simulation and training.

This module defines key parameters for:
- Folder and path configurations
- Simulation settings
- Drone and sensor characteristics 
- Map representation
- Training hyperparameters
- Neural network architecture
- Computational resource settings

Key configurations include:
- Number of agents
- Sensor ranges
- Map resolution
- Episode and training parameters
- GPU and logging options
"""

FOLDER_NAME = 'marvel'
LOAD_FOLDER_NAME = 'marvel'
model_path = f'model/{FOLDER_NAME}'
load_path = f'load_model/{LOAD_FOLDER_NAME}'
train_path = f'train/{FOLDER_NAME}'
gifs_path = f'gifs/{FOLDER_NAME}'

# save training data
SUMMARY_WINDOW = 32
LOAD_MODEL = True  # Set to true to use trained model in load_model folder
SAVE_IMG_GAP = 1000
NUM_EPISODE_BUFFER = 40

# Sim parameters
N_AGENTS = 4
USE_CONTINUOUS_SIM = True
NUM_SIM_STEPS = 6
VELOCITY = 1
YAW_RATE = 35 # in degrees

# Heading parameters
FOV = 120   # in degrees
V_FOV = 60
MOUNTING_ANGLE = 15 # downwards
NUM_ANGLES_BIN = 36
NUM_HEADING_CANDIDATES = 3
DRONE_HEIGHT = 2

# map and planning resolution
CELL_SIZE = 0.4  # meter
NODE_RESOLUTION = 4.0  # meter
FRONTIER_CELL_SIZE = 2 * CELL_SIZE

# map representation
FREE = 255
OCCUPIED = 1
UNKNOWN = 127

# sensor and utility range
SENSOR_RANGE = 10  # meter
UTILITY_RANGE = 0.9 * SENSOR_RANGE
MIN_UTILITY = 1

# updating map range w.r.t the robot
UPDATING_MAP_SIZE = 4 * SENSOR_RANGE + 4 * NODE_RESOLUTION

# training parameters
MAX_EPISODE_STEP = 128
REPLAY_SIZE = 10000
MINIMUM_BUFFER_SIZE = 2000
BATCH_SIZE = 256
LR = 1e-5
GAMMA = 1
NUM_META_AGENT = 18

# network parameters
NODE_INPUT_DIM = 6
EMBEDDING_DIM = 128

# Graph parameters
NUM_NODE_NEIGHBORS = 5
K_SIZE = NUM_NODE_NEIGHBORS**2   # the number of neighboring nodes
NODE_PADDING_SIZE = 360  # the number of nodes will be padded to this value

# GPU usage
USE_GPU = False  # do you want to collect training data using GPUs
USE_GPU_GLOBAL = True  # do you want to train the network using GPUs
NUM_GPU = 1

USE_WANDB = False
TRAIN_ALGO = 3
# 0: SAC, 1:MAAC , 2: Ground Truth 3: MAAC and Ground Truth
