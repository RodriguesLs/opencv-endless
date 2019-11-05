import cv2
import numpy as np 

cap = cv2.VideoCapture("/home/rodrigues/Documents/people-counting/videos/other_test.h264")
counter = -1
while True:
    ret, frame = cap.read()
    counter += 1
    if not ret:
        break

    if counter == 486:
        cv2.imwrite("img_test.jpg", frame)
        break
    # cv2.putText(frame, "{}".format(counter), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)

    # cv2.imshow("frame", frame)
    # key = cv2.waitKey(0)

    # if key == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()    