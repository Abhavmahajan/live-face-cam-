import cv2

img = cv2.imread("images/xDTRYSD5_66bs_1024.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (11, 11), 0)

edges = cv2.Canny(blur_img, 60, 60)

cv2.imshow("eeee", img)
cv2.imshow("gray_img", gray_img)
cv2.imshow("blur_img", blur_img)
cv2.imshow("edges", edges)

cv2.waitKey(0)