import cv2
import numpy as np
import matplotlib.pyplot as plt

# ── 1) Read and display both images side by side ──────────────────────────────

img1 = cv2.imread('chessboard_1.png')
img2 = cv2.imread('chessboard_2.png')

# Convert BGR → RGB for Matplotlib display
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img1_rgb)
axes[0].set_title('Chessboard 1')
axes[0].axis('off')

axes[1].imshow(img2_rgb)
axes[1].set_title('Chessboard 2')
axes[1].axis('off')

plt.tight_layout()
plt.show()


# ── 2) Function to count red, green, and blue pixels ─────────────────────────

def count_rgb_pixels(image):
    """
    Takes a BGR image (as loaded by OpenCV) and returns the count of
    red, green, and blue pixels individually.

    A pixel is classified as:
      - Red   : R channel is dominant AND G and B are low
      - Green : G channel is dominant AND R and B are low
      - Blue  : B channel is dominant AND R and G are low
    """
    b, g, r = cv2.split(image)

    threshold = 100   # minimum value for the dominant channel
    gap       = 50    # how much larger the dominant channel must be

    red_mask   = (r > threshold) & (r > g + gap) & (r > b + gap)
    green_mask = (g > threshold) & (g > r + gap) & (g > b + gap)
    blue_mask  = (b > threshold) & (b > r + gap) & (b > g + gap)

    return int(np.sum(red_mask)), int(np.sum(green_mask)), int(np.sum(blue_mask))


# Apply to both images and print results
for i, img in enumerate([img1, img2], start=1):
    red, green, blue = count_rgb_pixels(img)
    print(f"Image {i}:")
    print(f"  Red Pixels:   {red}")
    print(f"  Green Pixels: {green}")
    print(f"  Blue Pixels:  {blue}")
    print()


# ── 3) Generate the third chessboard ─────────────────────────────────────────

def generate_third_chessboard(image1, image2):
    """
    Compares corresponding pixels from both images and generates a third image:
      - If pixels at the same position are IDENTICAL → set to BLACK
      - If pixels are DIFFERENT → set to the AVERAGE colour of the two pixels
    Both images must be the same size.
    """
    assert image1.shape == image2.shape, "Images must be the same dimensions!"

    # Find positions where all three channels (B, G, R) are identical
    identical_mask = np.all(image1 == image2, axis=2)  # shape: (H, W) boolean

    # Compute the average colour for every pixel (rounded to nearest int)
    avg_image = ((image1.astype(np.uint16) + image2.astype(np.uint16)) // 2).astype(np.uint8)

    # Start with the averaged image, then zero out identical positions → black
    result = avg_image.copy()
    result[identical_mask] = [0, 0, 0]

    return result


# Generate and display all three images side by side
generated = generate_third_chessboard(img1, img2)
generated_rgb = cv2.cvtColor(generated, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img1_rgb)
axes[0].set_title('Chessboard 1')
axes[0].axis('off')

axes[1].imshow(img2_rgb)
axes[1].set_title('Chessboard 2')
axes[1].axis('off')

axes[2].imshow(generated_rgb)
axes[2].set_title('Generated Chessboard')
axes[2].axis('off')

plt.tight_layout()
plt.show()

# Optionally save the generated chessboard
cv2.imwrite('chessboard_generated.png', generated)
print("Generated chessboard saved as 'chessboard_generated.png'")