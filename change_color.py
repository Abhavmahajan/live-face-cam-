import cv2

# Use a raw string for Windows path
img = cv2.imread(r"C:\Users\abhav\OneDrive\Desktop\face d\images\kris12.27.22ig1.jpg")

# Check if the image was loaded
if img is None:
    print("Error: Image file not found.")
else:
    resized_img = cv2.resize(img, (600, 700))
    cv2.imshow("Resized Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
