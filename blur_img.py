import cv2

img = cv2.imread("images/xDTRYSD5_66bs_1024.png")

blur_img = cv2.GaussianBlur(img, (11, 11), 0)

cv2.imshow("hey", img)
cv2.imshow("blury mage", blur_img)

cv2.waitKey(0)