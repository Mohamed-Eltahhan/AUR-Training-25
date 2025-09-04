import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('shapes.jpg')
out = img.copy()

out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)

lower_blue = np.array([0, 0, 180])
upper_blue = np.array([100, 100, 255])
blue_mask = np.all((out >= lower_blue) & (out <= upper_blue), axis = -1)

lower_black = np.array([0, 0, 0])
upper_black = np.array([50, 50, 50])
black_mask = np.all((out >= lower_black) & (out <= upper_black), axis = -1)

lower_red = np.array([180, 0, 0])
upper_red = np.array([255, 100, 100])
red_mask = np.all((out >= lower_red) & (out <= upper_red), axis = -1)

out[blue_mask] = [0, 0, 0]
out[red_mask] = [0, 0, 255]
out[black_mask] = [255, 0, 0]



fig, axes = plt.subplots(1, 2)
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(out)
axes[1].set_title('Processed Image')
axes[1].axis('off')
plt.show()