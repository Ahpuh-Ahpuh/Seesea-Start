from djitellopy import Tello
import cv2
import time
import threading
import os

drone = Tello()
drone.connect()
drone.takeoff()
drone.streamon()


#Check battery
def bat():
    while True:
        time.sleep(10)
        print(drone.get_battery())
        if drone.get_battery()<30:
            drone.land()
            break
    os._exit(1)
c = threading.Thread(name='background', target=bat)
c.start()


def mystream():
    while True:
        myFrame = drone.get_frame_read()
        myFrame = myFrame.frame
        img = cv2.resize(myFrame,(720,480))
        cv2.imshow('Imagen',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            drone.land()
            break
    os._exit(1)
b = threading.Thread(name='background', target=mystream)
b.start()



#위치 제어를 위한 PID control
Kp = 2
Ki = 0.1
tiempo = []      #초기화
height = []
error = []
sumatoria = 0
desired_height = 120
tiempo.append(time.clock())
height.append(drone.get_distance_tof())
time.sleep(0.15)
tiempo.append(time.clock())
height.append(drone.get_distance_tof())
error.append(desired_height-height[-1])

while True:        #Ciclo infinito
    height.append(drone.get_distance_tof())
    tiempo.append(time.clock())
    error.append(desired_height-height[-1])
    deltaError = error[-1]-error[-2]
    deltatiempo = tiempo[-1]-tiempo[-2]
    sumatoria = sumatoria+(tiempo[-1]-tiempo[-2])*(error[-1]-error[-2])
    vel_updown=Kp*error[-1]+Ki*sumatoria+Kd*(deltaError/deltatiempo)
    drone.send_rc_control(0, 0, round(vel_updown), 0)
    time.sleep(0.1)
