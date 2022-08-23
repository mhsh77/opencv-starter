import cv2
# import the opencv library
cap = cv2.VideoCapture(0)
# choosing source of video
while True:

    _, frame = cap.read()
    # getting frames of video

    cv2.imshow('frame name', frame)
    # showing frame in a window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # waiting for q to close app
        break
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
