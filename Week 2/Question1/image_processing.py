import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(path):

    img = cv2.imread(path)

    if img is None:
        print("Image not found")
        return

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Original Image
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    plt.imshow(gray,cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()

    # Histogram
    plt.hist(gray.ravel(), bins=256)
    plt.title("Histogram")
    plt.show()

    # Resize
    resized = cv2.resize(img, (300,300))

    plt.imshow(resized)
    plt.title("Resized Image")
    plt.axis("off")
    plt.show()

    # Edge Detection
    edges = cv2.Canny(gray,100,200)

    plt.imshow(edges, cmap="gray")
    plt.title("Edge Detection")
    plt.axis("off")
    plt.show()

    # Add Noise
    noise = np.random.normal(0,25,gray.shape)

    noisy = gray + noise
    noisy = np.clip(noisy,0,255).astype(np.uint8)

    plt.imshow(noisy,cmap="gray")
    plt.title("Noisy Image")
    plt.axis("off")
    plt.show()

    # Gaussian Filter
    filtered = cv2.GaussianBlur(noisy,(5,5),0)

    plt.imshow(filtered,cmap="gray")
    plt.title("Gaussian Filter Output")
    plt.axis("off")
    plt.show()


process_image("image1.jpg")
process_image("image2.jpg")