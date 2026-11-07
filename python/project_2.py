import cv2
import time
import serial

arduino=serial.Serial('COM3',9600,timeout=0)

arduino.reset_input_buffer()
time.sleep(2)

vide0=cv2.VideoCapture(0)

print("bring the object  infront camera to open the led light ")
print("bring red object infront of camera to open red led")
print("bring blue object infront of camera to open blue led")
print("bring yellow object infront of camera to open yellow led")

try:
    while True:
        ret,frame=vide0.read()
        
        if not ret:
            
            print("camera could not loaded")
        else:
            
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            
            
            lower_red=(0, 100, 100)
            upper_red=(10,255,255)
            
            red_mask=cv2.inRange(hsv,lower_red,upper_red)
            
            
            
            red_contours,hirarchy=cv2.findContours(red_mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
            
            lower_blue=(110, 50, 50)
            upper_blue=(130, 255, 255)
                        
            blue_mask=cv2.inRange(hsv,lower_blue,upper_blue)
            
            blue_contours,hirarchy=cv2.findContours(blue_mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
            
            lower_yellow=(20, 100, 100)
            upper_yellow=(35, 255, 255)
            yellow_mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
            
            yellow_contours,hirarchy=cv2.findContours(blue_mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
            
            
            if len(red_contours)>0:
                red_large_area=max(red_contours,key=cv2.contourArea)
                
                red_area=cv2.contourArea(red_large_area)
                
                if red_area>500:
                    arduino.write(b'r')
                    print("red light on")
                    M=cv2.moments(red_large_area)
                    if M["m00"] != 0:
                                red_x = int(M["m10"] / M["m00"])
                                red_y = int(M["m01"] / M["m00"])
                                    
                                print("Object X =", red_x)
                                print("Object Y =", red_y)
                                
                                
                                cv2.circle(frame,(red_x,red_y),10,(0,0,0),1)
                                cv2.putText(frame,f"x={red_x},y={red_y}",(red_x+10,red_y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
            
            elif len(blue_contours)>0:
                            blue_large_area=max(blue_contours,key=cv2.contourArea)
                            
                            blue_area=cv2.contourArea(blue_large_area)
                            
                            if blue_area>500:
                                arduino.write(b'b')
                                print("blue light on")
                                M=cv2.moments(blue_large_area)
                                if M["m00"] != 0:
                                    blue_x = int(M["m10"] / M["m00"])
                                    blue_y = int(M["m01"] / M["m00"])
                                                                    
                                    print("Object X =", blue_x)
                                    print("Object Y =", blue_y)
                                                                
                                                                
                                    cv2.circle(frame,(blue_x,blue_y),10,(0,0,0),1)
                                    cv2.putText(frame,f"x={blue_x},y={blue_y}",(blue_x+10,blue_y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
                                
            elif len(yellow_contours)>0:
                            yellow_large_area=max(red_contours,key=cv2.contourArea)
                            
                            yellow_area=cv2.contourArea(yellow_large_area)
                            
                            if yellow_area>500:
                                arduino.write(b'r')
                                print("yellow light on")
                                M=cv2.moments(red_large_area)
                                if M["m00"] != 0:
                                    yellow_x = int(M["m10"] / M["m00"])
                                    yellow_y = int(M["m01"] / M["m00"])
                                                                    
                                    print("Object X =", yellow_x)
                                    print("Object Y =", yellow_y)
                                                                
                                                                
                                    cv2.circle(frame,(yellow_x,yellow_y),10,(0,0,0),1)
                                    cv2.putText(frame,f"x={yellow_x},y={yellow_y}",(yellow_x+10,yellow_y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
            else:
                  arduino.write(b'0')
            cv2.imshow("retector",frame)
            cv2.imshow("red_mask",red_mask)
            cv2.imshow("yellow_mask",yellow_mask)
            cv2.imshow("blue_mask",blue_mask)
            
            if cv2.waitKey(1)==ord("q"):
                print("quiting.....")
                break
            
finally:
    vide0.release()
    cv2.destroyAllWindows()
    arduino.close()
    print("arduino close.....")
                             
                                    
                                    
                                
                                
                            
                    