import cv2
import numpy as np

# Parameters
RELATIVE_PATH = 'asdf/test_z_variations_blade30_dagan_experiment_default_9_4.png'
PHOTO_HEIGHT = 128
PHOTO_WIDTH = 128

total_image = cv2.imread(RELATIVE_PATH) 

original = total_image[0:PHOTO_HEIGHT, 0:PHOTO_WIDTH].astype(int)
generated = total_image[0:PHOTO_HEIGHT, PHOTO_WIDTH:2*PHOTO_WIDTH].astype(int)

subtracted = np.subtract(original, generated)
normalized = np.add(subtracted, 128)

cv2.imwrite('final.png', np.concatenate((original, generated, normalized), axis=1)) 
