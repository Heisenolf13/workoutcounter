
import cv2
import numpy
import time

def nothing(x):
    pass

cap = cv2.VideoCapture(1)

# cv2.namedWindow("frame")
# cv2.createTrackbar("test", "frame", 50, 500, nothing)


counter = 0
a = 0
while True:
    blank_image = numpy.zeros((600,800,3), numpy.uint8)
    _, frame =cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = numpy.array([94,80,2])
    upper_blue = numpy.array([126,255,255])
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # test = cv2.getTrackbarPos("test", "frame")

    c1 = counter
    # if not a % 35:
    if cv2.countNonZero(mask) > 5000:
        counter += 1
        # a +=1
    # else:
        # a +=1
    c2 = counter
    if c1 != c2:
        time.sleep(2.5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_image, str(counter), (50,300), font, 10, (255,255,255), 10)#BGR
    #cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    cv2.imshow("a", blank_image)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()








    # font = cv2.FONT_HERSHEY_COMPLEX
    # cv2.putText(frame, str(test), (50,150), font, 4, (255,0,0))#BGR

"""
# Loading modules
import cv2
import numpy as np     # Numpy module will be used for horizontal stacking of two frames

video=cv2.VideoCapture(1)
a=0
while True:
    a=a+1
    check, frame= video.read()

    # Converting the input frame to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   

    # Fliping the image as said in question
    gray_flip = cv2.flip(gray,1)

    # Combining the two different image frames in one window
    combined_window = np.hstack([gray,gray_flip])

    # Displaying the single window
    cv2.imshow("Combined videos ",combined_window)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print(a)

video.release()
cv2.destroyAllWindows
"""
