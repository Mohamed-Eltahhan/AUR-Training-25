import numpy as np
import matplotlib.pyplot as plt
import cv2

def convolve(image, kernel):
    kernel_l, kernel_w = kernel.shape
    if (kernel_l != kernel_w) or (kernel_l % 2 == 0):
        raise ValueError('Invalid kernel')
    image_l, image_w = image.shape
    flipped_k = np.flipud(np.fliplr(kernel))
    padded_i = np.pad(image, (kernel_l // 2,kernel_l // 2), 'edge')
    output = np.zeros_like(image)
    for i in range(image_l):
        for j in range(image_w):
            patch = padded_i[i:i+kernel_l , j:j+kernel_w]
            output[i,j] = np.sum(patch * flipped_k)
    return output



img = cv2.imread('image.jpg', cv2. IMREAD_GRAYSCALE)
fig, axes = plt.subplots (2, 2, figsize=(8, 8))
axes [0, 0].imshow(img, cmap='gray')
axes [0, 0].set_title('Original Image')
axes [0, 0].axis('off')
axes [0, 1].imshow(convolve(img, np.ones ((5, 5)) / 25 ) , cmap='gray')
axes [0, 1].set_title('Box Filter')
axes [0, 1].axis('off')
axes [1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0,2], [-1,0,1]])), cmap='gray')
axes [1, 0].set_title('Horizontal Sobel Filter')
axes [1, 0].axis('off')
axes [1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0,0,0], [1, 2, 1]])), cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes [1, 1].axis('off')
plt.show()