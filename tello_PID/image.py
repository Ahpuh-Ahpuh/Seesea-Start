from djitellopy import tello
import cv2

drone=tello.Tello()
drone.connect()

print(drone.get_battery())

drone.streamon()
while True:
    img=drone.get_frame_read().frame
    img=cv2.resize(img,(360,240))
    cv2.imshow("Image",img)
    cv2.waitKey(1)
