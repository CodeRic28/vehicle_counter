from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
# import argparse
#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# ap.add_argument("-p", "--prototxt", required=True,
# 	help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", required=True,
# 	help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.2,
# 	help="minimum probability to filter weak detections")
# args = vars(ap.parse_args())

VIDEOS_DIR = os.path.join('.', 'videos')

video_path = os.path.join(VIDEOS_DIR, 'Vehicle_count_test.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
cap.set(3,1280)
cap.set(4,720)
# out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'model','runs', 'detect', 'train', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model
classnames = ['Auto','Bus','Tempo_traveller','Tractor','Truck']

mask = cv2.imread("mask.png")
mask = cv2.resize(mask, (1280,720))

# Tracking
tracker = Sort(max_age=20, min_hits=3,iou_threshold=0.3)

limits = [50, 300, 1270,295]
vehicleCount = {}
for cls in classnames:
    vehicleCount[cls] = 0
print(vehicleCount)
'''
    List to check if ID has been counted or not
    If ID is not present in the list, append and increase count
    If ID is present in the list, dont increase count
'''
idTrackCount = []

threshold = 0.20
success = True
cls = 0
while success:

    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img, (1280,720))
    imgRegion = cv2.bitwise_and(img,mask)
    results = model(imgRegion)

    detections = np.empty((0,5))

    # results = model(img)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding box
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            w, h = x2-x1,y2-y1
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            currentArray = np.array([x1,y1,x2,y2,conf])
            detections = np.vstack((detections, currentArray))

    cv2.line(img, (limits[0],limits[1]), (limits[2],limits[3]),(0,0,255),5)
    resultsTracker = tracker.update(detections)
    for result in resultsTracker:
        x1,y1,x2,y2,id = result
        x1, y1, x2, y2, id = int(x1),int(y1),int(x2),int(y2),int(id)
        w, h = x2 - x1, y2 - y1
        print(result)

        cx, cy = x1+w//2,y1+h//2
        cv2.circle(img,(cx,cy),4,(255,0,0),cv2.FILLED)

        if limits[0]<cx<limits[2] and limits[1]-30<cy<limits[1]+30:
            if id not in idTrackCount:
                vehicleCount[classnames[cls]]+=1
                idTrackCount.append(id)
        print(classnames[cls], vehicleCount[classnames[cls]])
        # print(classnames[cls])
        cvzone.cornerRect(img, (x1, y1, w, h))
    cvzone.putTextRect(img, f'{classnames[cls]}', (max(0, x1), max(35, y1)), scale=3, thickness=3)
    cvzone.putTextRect(img, f"Auto: {vehicleCount['Auto']}", (50,50), scale=2, thickness=2)
    cvzone.putTextRect(img, f"Bus: {vehicleCount['Bus']}", (50, 100), scale=2, thickness=2)
    cvzone.putTextRect(img, f"Tempo Traveller: {vehicleCount['Tempo_traveller']}", (50, 150), scale=2, thickness=2)
    cvzone.putTextRect(img, f"Tractor: {vehicleCount['Tractor']}", (50, 200), scale=2, thickness=2)
    cvzone.putTextRect(img, f"Truck: {vehicleCount['Truck']}", (50, 250), scale=2, thickness=2)

    cv2.imshow("img", img)
    # cv2.imshow("imgRegion",imgRegion)
    cv2.waitKey(1)

cap.release()

cv2.destroyAllWindows()