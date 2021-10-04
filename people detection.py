import cv2
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture('in.avi')
# cap = cv2.VideoCapture('video.mp4')
# cap = cv2.VideoCapture('video1.mp4')
# def setValues(x):
#    print("")

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# human_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
# cv2.namedWindow("Color detectors")
# cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
# cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
# cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
# cv2.createTrackbar("Lower Hue", "Color detectors", 4, 180,setValues)
# cv2.createTrackbar("Lower Saturation", "Color detectors", 172, 255,setValues)
# cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)

while(True):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    humans = human_cascade.detectMultiScale(gray, 1.5, 1)
    
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
         
    # cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
