import cv2

capture = cv2.VideoCapture(0)

while True:
    is_True, frame = capture.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("my webcam", frame)
    cv2.imshow("HLS video", gray_img)

    if cv2.waitKey(20) & 0xff == ord("e"):
        break