import cv2

myimg = cv2.imread("images/contact us imagee.png")

resized_img = cv2.resize(myimg, (1500, 500))

cv2.imshow("eeeeee", resized_img)
cv2.imshow("rrrrrr",myimg)

cv2.waitKey(0)